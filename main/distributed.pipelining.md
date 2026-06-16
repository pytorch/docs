# Pipeline Parallelism

Note

`torch.distributed.pipelining` is currently in alpha state and under
development. API changes may be possible. It was migrated from the [PiPPy](https://github.com/pytorch/PiPPy) project.

## Why Pipeline Parallel?

Pipeline Parallelism is one of the primitive forms of parallelism for deep learning.
It allows the **execution** of a model to be partitioned such that multiple
**micro-batches** can execute different parts of the model code concurrently.
Pipeline parallelism can be an effective technique for:

- large-scale training
- bandwidth-limited clusters
- large model inference

The above scenarios share a commonality that the computation per device cannot
hide the communication of conventional parallelism, for example, the weight
all-gather of FSDP.

## What is `torch.distributed.pipelining`?

While promising for scaling, pipelining is often difficult to implement because
it needs to **partition the execution** of a model in addition to model weights.
The partitioning of execution often requires intrusive code changes to your
model. Another aspect of complexity comes from **scheduling micro-batches in a
distributed environment**, with **data flow dependency** considered.

The `pipelining` package provides a toolkit that does said things
**automatically** which allows easy implementation of pipeline parallelism
on **general** models.

It consists of two parts: a
**splitting frontend** and a **distributed runtime**.
The splitting frontend takes your model code as-is, splits it up into "model
partitions", and captures the data-flow relationship. The distributed runtime
executes the pipeline stages on different devices in parallel, handling things
like micro-batch splitting, scheduling, communication, and gradient propagation,
etc.

Overall, the `pipelining` package provides the following features:

- Splitting of model code based on simple specification.
- Rich support for pipeline schedules, including GPipe, 1F1B,
Interleaved 1F1B and Looped BFS, and providing the infrastructure for writing
customized schedules.
- First-class support for cross-host pipeline parallelism, as this is where PP
is typically used (over slower interconnects).
- Composability with other PyTorch parallel techniques such as data parallel
(DDP, FSDP) or tensor parallel. The [TorchTitan](https://github.com/pytorch/torchtitan) project demonstrates a "3D parallel"
application on the Llama model.

## Step 1: build `PipelineStage`

Before we can use a `PipelineSchedule`, we need to create `PipelineStage`
objects that wrap the part of the model running in that stage. The
`PipelineStage` is responsible for allocating communication buffers and
creating send/recv ops to communicate with its peers. It manages intermediate
buffers e.g. for the outputs of forward that have not been consumed yet, and it
provides a utility for running the backwards for the stage model.

A `PipelineStage` needs to know the input and output shapes for the stage
model, so that it can correctly allocate communication buffers. The shapes must
be static, e.g. at runtime the shapes can not change from step to step. A class
`PipeliningShapeError` will be raised if runtime shapes do not match the
expected shapes. When composing with other parallelisms or applying mixed
precision, these techniques must be taken into account so the `PipelineStage`
knows the correct shape (and dtype) for the output of the stage module at
runtime.

Users may construct a `PipelineStage` instance directly, by passing in an
`nn.Module` representing the portion of the model that should run on the
stage. This may require changes to the original model code. See the example
in Option 1: splitting a model manually.

Alternatively, the splitting frontend can use graph partitioning to split your
model into a series of `nn.Module` automatically. This technique requires the
model is traceable with `torch.Export`. Composability of the resulting
`nn.Module` with other parallelism techniques is experimental, and may require
some workarounds. Usage of this frontend may be more appealing if the user
cannot easily change the model code. See Option 2: splitting a model automatically for more
information.

## Step 2: use `PipelineSchedule` for execution

We can now attach the `PipelineStage` to a pipeline schedule, and run the
schedule with input data. Here is a GPipe example:

```
from torch.distributed.pipelining import ScheduleGPipe

# Create a schedule
schedule = ScheduleGPipe(stage, n_microbatches)

# Input data (whole batch)
x = torch.randn(batch_size, in_dim, device=device)

# Run the pipeline with input `x`
# `x` will be divided into microbatches automatically
if rank == 0:
 schedule.step(x)
else:
 output = schedule.step()
```

Note that the above code needs to be launched for each worker, thus we use a
launcher service to launch multiple processes:

```
torchrun --nproc_per_node=2 example.py
```

## Options for Splitting a Model

### Option 1: splitting a model manually

To directly construct a `PipelineStage`, the user is responsible for providing
a single `nn.Module` instance that owns the relevant `nn.Parameters` and
`nn.Buffers`, and defines a `forward()` method that executes the operations
relevant for that stage. For example, a condensed version of the Transformer
class defined in Torchtitan shows a pattern of building an easily partitionable
model.

```
class Transformer(nn.Module):
 def __init__(self, model_args: ModelArgs):
 super().__init__()

 self.tok_embeddings = nn.Embedding(...)

 # Using a ModuleDict lets us delete layers without affecting names,
 # ensuring checkpoints will correctly save and load.
 self.layers = torch.nn.ModuleDict()
 for layer_id in range(model_args.n_layers):
 self.layers[str(layer_id)] = TransformerBlock(...)

 self.output = nn.Linear(...)

 def forward(self, tokens: torch.Tensor):
 # Handling layers being 'None' at runtime enables easy pipeline splitting
 h = self.tok_embeddings(tokens) if self.tok_embeddings else tokens

 for layer in self.layers.values():
 h = layer(h, self.freqs_cis)

 h = self.norm(h) if self.norm else h
 output = self.output(h).float() if self.output else h
 return output
```

A model defined in this manner can be easily configured per stage by first
initializing the whole model (using meta-device to avoid OOM errors), deleting
undesired layers for that stage, and then creating a PipelineStage that wraps
the model. For example:

```
with torch.device("meta"):
 assert num_stages == 2, "This is a simple 2-stage example"

 # we construct the entire model, then delete the parts we do not need for this stage
 # in practice, this can be done using a helper function that automatically divides up layers across stages.
 model = Transformer()

 if stage_index == 0:
 # prepare the first stage model
 del model.layers["1"]
 model.norm = None
 model.output = None

 elif stage_index == 1:
 # prepare the second stage model
 model.tok_embeddings = None
 del model.layers["0"]

 from torch.distributed.pipelining import PipelineStage
 stage = PipelineStage(
 model,
 stage_index,
 num_stages,
 device,
 )
```

When composing with other Data or Model parallelism techniques, `output_args`
may also be required, if the output shape/dtype of the model chunk will be
affected.

### Option 2: splitting a model automatically

If you have a full model and do not want to spend time on modifying it into a
sequence of "model partitions", the `pipeline` API is here to help.
Here is a brief example:

```
class Model(torch.nn.Module):
 def __init__(self) -> None:
 super().__init__()
 self.emb = torch.nn.Embedding(10, 3)
 self.layers = torch.nn.ModuleList(
 Layer() for _ in range(2)
 )
 self.lm = LMHead()

 def forward(self, x: torch.Tensor) -> torch.Tensor:
 x = self.emb(x)
 for layer in self.layers:
 x = layer(x)
 x = self.lm(x)
 return x
```

If we print the model, we can see multiple hierarchies, which makes it hard to split by hand:

```
Model(
 (emb): Embedding(10, 3)
 (layers): ModuleList(
 (0-1): 2 x Layer(
 (lin): Linear(in_features=3, out_features=3, bias=True)
 )
 )
 (lm): LMHead(
 (proj): Linear(in_features=3, out_features=3, bias=True)
 )
)
```

Let us see how the `pipeline` API works:

```
from torch.distributed.pipelining import pipeline, SplitPoint

# An example micro-batch input
x = torch.LongTensor([1, 2, 4, 5])

pipe = pipeline(
 module=mod,
 mb_args=(x,),
 split_spec={
 "layers.1": SplitPoint.BEGINNING,
 }
)
```

The `pipeline` API splits your model given a `split_spec`, where
`SplitPoint.BEGINNING` stands for adding a split point
*before* execution of certain submodule in the `forward` function, and
similarly, `SplitPoint.END` for split point *after* such.

If we `print(pipe)`, we can see:

```
GraphModule(
 (submod_0): GraphModule(
 (emb): InterpreterModule()
 (layers): Module(
 (0): InterpreterModule(
 (lin): InterpreterModule()
 )
 )
 )
 (submod_1): GraphModule(
 (layers): Module(
 (1): InterpreterModule(
 (lin): InterpreterModule()
 )
 )
 (lm): InterpreterModule(
 (proj): InterpreterModule()
 )
 )
)

def forward(self, x):
 submod_0 = self.submod_0(x); x = None
 submod_1 = self.submod_1(submod_0); submod_0 = None
 return (submod_1,)
```

The "model partitions" are represented by submodules (`submod_0`,
`submod_1`), each of which is reconstructed with original model operations, weights
and hierarchies. In addition, a "root-level" `forward` function is
reconstructed to capture the data flow between those partitions. Such data flow
will be replayed by the pipeline runtime later, in a distributed fashion.

The `Pipe` object provides a method for retrieving the "model partitions":

```
stage_mod : nn.Module = pipe.get_stage_module(stage_idx)
```

The returned `stage_mod` is a `nn.Module`, with which you can create an
optimizer, save or load checkpoints, or apply other parallelisms.

`Pipe` also allows you to create a distributed stage runtime on a device given
a `ProcessGroup`:

```
stage = pipe.build_stage(stage_idx, device, group)
```

Alternatively, if you would like to build the stage runtime later after some
modification to the `stage_mod`, you can use a functional version of the
`build_stage` API. For example:

```
from torch.distributed.pipelining import build_stage
from torch.nn.parallel import DistributedDataParallel

dp_mod = DistributedDataParallel(stage_mod)
info = pipe.info()
stage = build_stage(dp_mod, stage_idx, info, device, group)
```

Note

The `pipeline` frontend uses a tracer (`torch.export`) to capture your
model into a single graph. If your model is not full-graph'able, you can use
our manual frontend below.

## Hugging Face Examples

In the [PiPPy](https://github.com/pytorch/PiPPy) repo where this package was
original created, we kept examples based on unmodified Hugging Face models.
See the [examples/huggingface](https://github.com/pytorch/PiPPy/tree/main/examples/huggingface) directory.

Examples include:

- [GPT2](https://github.com/pytorch/PiPPy/tree/main/examples/huggingface/pippy_gpt2.py)
- [Llama](https://github.com/pytorch/PiPPy/tree/main/examples/llama)

## Technical Deep Dive

### How does the `pipeline` API split a model?

First, the `pipeline` API turns our model into a directed acyclic graph (DAG)
by tracing the model. It traces the model using `torch.export` - a PyTorch 2
full-graph capturing tool.

Then, it groups together the **operations and parameters** needed by a stage
into a reconstructed submodule: `submod_0`, `submod_1`, ...

Different from conventional submodule access methods like `Module.children()`,
the `pipeline` API does not only cut the module structure of your model, but
also the **forward** function of your model.

This is necessary because model structure like `Module.children()` merely
captures information during `Module.__init__()`, and does not capture any
information about `Module.forward()`. Said differently, `Module.children()`
lacks information about the following aspects key to pipelininig:

- Execution order of child modules in `forward`
- Activation flows between child modules
- Whether there are any functional operators between child modules (for example,
`relu` or `add` operations will not be captured by `Module.children()`).

The `pipeline` API, on the contrary, makes sure that the `forward` behavior
is truly preserved. It also captures the activation flow between the partitions,
helping the distributed runtime to make correct send/receive calls without human
intervention.

Another flexibility of the `pipeline` API is that split points can be at
arbitrary levels within your model hierarchy. In the split partitions, the original model
hierarchy related to that partition will be reconstructed at no cost to you.
At a result, fully-qualified names (FQNs) pointing to a submodule or parameter
would be still valid, and services that relies on FQNs (such as FSDP, TP or
checkpointing) can still run with your partitioned modules with almost zero code
change.

## Implementing Your Own Schedule

You can implement your own pipeline schedule by extending one of the following two classes:

- `PipelineScheduleSingle`
- `PipelineScheduleMulti`

`PipelineScheduleSingle` is for schedules that assigns *only one* stage per rank.
`PipelineScheduleMulti` is for schedules that assigns multiple stages per rank.

For example, `ScheduleGPipe` and `Schedule1F1B` are subclasses of `PipelineScheduleSingle`.
Whereas, `ScheduleInterleaved1F1B`, `ScheduleLoopedBFS`, `ScheduleInterleavedZeroBubble`, and `ScheduleZBVZeroBubble`
are subclasses of `PipelineScheduleMulti`.

## Logging

You can turn on additional logging using the `TORCH_LOGS` environment variable from [torch._logging](https://pytorch.org/docs/main/logging.html#module-torch._logging):

- `TORCH_LOGS=+pp` will display `logging.DEBUG` messages and all levels above it.
- `TORCH_LOGS=pp` will display `logging.INFO` messages and above.
- `TORCH_LOGS=-pp` will display `logging.WARNING` messages and above.

## API Reference

### Model Split APIs

The following set of APIs transform your model into a pipeline representation.

*class*torch.distributed.pipelining.SplitPoint(*value*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/_IR.py#L1192)

Enum representing the points at which a split can occur in the execution of a submodule.
:ivar BEGINNING: Represents adding a split point *before* the execution of a certain submodule in the forward function.
:ivar END: Represents adding a split point *after* the execution of a certain submodule in the forward function.

torch.distributed.pipelining.pipeline(*module*, *mb_args*, *mb_kwargs=None*, *split_spec=None*, *split_policy=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/_IR.py#L1247)

Split a module based on a specification.

See Pipe for more details.

Parameters:

- **module** ([*Module*](generated/torch.nn.Module.html#torch.nn.Module)) - The module to be split.
- **mb_args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,**...**]*) - Example positional inputs, in micro-batch form.
- **mb_kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Example keyword inputs, in micro-batch form. (default: None)
- **split_spec** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**SplitPoint**]**|**None*) - A dictionary using submodule names as split marker. (default: None)
- **split_policy** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[*[*GraphModule*](fx.html#torch.fx.GraphModule)*]**,*[*GraphModule*](fx.html#torch.fx.GraphModule)*]**|**None*) - The policy to use for splitting the module. (default: None)

Return type:

A pipeline representation of class Pipe.

*class*torch.distributed.pipelining.Pipe(*split_gm*, *num_stages*, *has_loss_and_backward*, *loss_spec*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/_IR.py#L561)

torch.distributed.pipelining.pipe_split()[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/_IR.py#L363)

pipe_split is a special operator that is used to mark the boundary between
stages in a module. It is used to split the module into stages. It is a
no-op if your annotated module is run eagerly.

Example

```
>>> def forward(self, x):
>>> x = torch.mm(x, self.mm_param)
>>> x = torch.relu(x)
>>> pipe_split()
>>> x = self.lin(x)
>>> return x
```

The above example will be split into two stages.

### Microbatch Utilities

*class*torch.distributed.pipelining.microbatch.TensorChunkSpec(*split_dim*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/microbatch.py#L60)

Class used to specify chunking of inputs

torch.distributed.pipelining.microbatch.split_args_kwargs_into_chunks(*args*, *kwargs*, *chunks*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/microbatch.py#L378)

Given a sequence of args and kwargs, split them into a number of chunks
according to their respective chunking specs.

Parameters:

- **args** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,**...**]*) - Tuple of args
- **kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]**|**None*) - Dict of kwargs
- **chunks** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Number of chunks to split the args and kwargs into
- **args_chunk_spec** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[**TensorChunkSpec**,**...**]**|**None*) - chunking specs for args, in same shape as args
- **kwargs_chunk_spec** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**TensorChunkSpec**]**|**None*) - chunking specs for kwargs, in same shape as kwargs

Returns:

List of sharded args
kwargs_split: List of sharded kwargs

Return type:

args_split

torch.distributed.pipelining.microbatch.merge_chunks(*chunks*, *chunk_spec*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/microbatch.py#L493)

Given a list of chunks, merge them into a single value according to
the chunk spec.

Parameters:

- **chunks** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) - list of chunks
- **chunk_spec** - Chunking spec for the chunks

Returns:

Merged value

Return type:

value

### Pipeline Stages

*class*torch.distributed.pipelining.stage.PipelineStage(*submodule*, *stage_index*, *num_stages*, *device*, *input_args=None*, *output_args=None*, *output_grads=None*, *input_grads=None*, *group=None*, *dw_builder=None*, *get_mesh=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/stage.py#L1639)

A pipeline stage for pipeline parallelism with sequential model partitioning.

Supports both **static** and **dynamic** metadata inference:

Static mode:

All of `input_args`, `output_args` (and `input_grads`/`output_grads`
when DTensors are present) are provided at construction time.

Dynamic mode:

Metadata is inferred from the first microbatch at runtime; any
statically provided args are used for validation only.

Parameters:

- **submodule** ([*Module*](generated/torch.nn.Module.html#torch.nn.Module)) - The `nn.Module` wrapped by this stage.
- **stage_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Zero-based stage ID.
- **num_stages** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Total number of stages in the pipeline.
- **device** ([*device*](tensor_attributes.html#torch.device)) - Device this stage runs on.
- **input_args** ([*Tensor*](tensors.html#torch.Tensor)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Tensor*](tensors.html#torch.Tensor)*,**...**]**|**None*) - Example input tensors (single tensor or tuple). Optional.
- **output_args** ([*Tensor*](tensors.html#torch.Tensor)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Tensor*](tensors.html#torch.Tensor)*,**...**]**|**None*) - Example output tensors. Optional.
- **output_grads** ([*Tensor*](tensors.html#torch.Tensor)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Tensor*](tensors.html#torch.Tensor)*|**None**,**...**]**|**None*) - Example output gradients (received from next stage). Optional.
- **input_grads** ([*Tensor*](tensors.html#torch.Tensor)*|*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*Tensor*](tensors.html#torch.Tensor)*|**None**,**...**]**|**None*) - Example input gradients (sent to previous stage). Optional.
- **group** ([*ProcessGroup*](distributed._dist2.html#torch.distributed._dist2.ProcessGroup)*|**None*) - Process group for P2P communication. Defaults to the
world process group.
- **dw_builder** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**]**,*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**...**]**,**None**]**]**|**None*) - Builder for deferred weight-update runners used by
zero-bubble (F/I/W) schedules.
- **get_mesh** (*GetMeshCallback**|**None*) - GetMeshCallback used during
dynamic DTensor inference. Ignored in fully static DTensor mode.

torch.distributed.pipelining.stage.build_stage(*stage_module*, *stage_index*, *pipe_info*, *device*, *group=None*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/stage.py#L1609)

Create a pipeline stage given a stage_module to be wrapped by this stage
and pipeline information.

Parameters:

- **stage_module** ([*torch.nn.Module*](generated/torch.nn.Module.html#torch.nn.Module)) - the module to be wrapped by this stage
- **stage_index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the index of this stage in the pipeline
- **pipe_info** (*PipeInfo*) - information about the pipeline, can be retrieved by pipe.info()
- **device** ([*torch.device*](tensor_attributes.html#torch.device)) - the device to be used by this stage
- **group** (*Optional**[**dist.ProcessGroup**]*) - the process group to be used by this stage

Returns:

a pipeline stage that can run with PipelineSchedules.

Return type:

_PipelineStage

### Pipeline Schedules

*class*torch.distributed.pipelining.schedules.ScheduleGPipe(*stage*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L872)

The GPipe schedule.
Will go through all the microbatches in a fill-drain manner.

*class*torch.distributed.pipelining.schedules.Schedule1F1B(*stage*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L995)

The 1F1B schedule.
Will perform one forward and one backward on the microbatches in steady state.

*class*torch.distributed.pipelining.schedules.ScheduleInterleaved1F1B(*stages*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*, *backward_requires_autograd=True*, *defer_pp_recv=False*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L2891)

The Interleaved 1F1B schedule.
See [https://arxiv.org/pdf/2104.04473](https://arxiv.org/pdf/2104.04473) for details.
Will perform one forward and one backward on the microbatches in steady
state and supports multiple stages per rank. When microbatches are ready for
multiple local stages, Interleaved 1F1B prioritizes the earlier microbatch
(also called "depth first").

This schedule is mostly similar to the original paper.
It differs by being relaxing the requirement of num_microbatch % pp_size == 0.
Using the flex_pp schedule, we will have num_rounds = max(1, n_microbatches // pp_group_size) and
it works as long as n_microbatches % num_rounds is 0. As a few examples, support

1. pp_group_size = 4, n_microbatches = 10. We will have num_rounds = 2 and n_microbatches % 2 is 0.
2. pp_group_size = 4, n_microbatches = 3. We will have num_rounds = 1 and n_microbatches % 1 is 0.

*class*torch.distributed.pipelining.schedules.ScheduleLoopedBFS(*stages*, *n_microbatches*, *loss_fn=None*, *output_merge_spec=None*, *scale_grads=True*, *backward_requires_autograd=True*, *defer_pp_recv=False*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L2664)

Breadth-First Pipeline Parallelism.
See [https://arxiv.org/abs/2211.05953](https://arxiv.org/abs/2211.05953) for details.
Similar to Interleaved 1F1B, Looped BFS supports multiple stages per rank.
What is different is that when microbatches are ready for multiple local
stages, Loops BFS will prioritizes the earlier stage, running all available
microbatches at once.

*class*torch.distributed.pipelining.schedules.ScheduleInterleavedZeroBubble(*stages*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*, *backward_requires_autograd=True*, *defer_pp_recv=False*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L3007)

The Interleaved Zero Bubble schedule.
See [https://arxiv.org/pdf/2401.10241](https://arxiv.org/pdf/2401.10241) for details.
Will perform one forward and one backward on inputs for the microbatches in steady
state and supports multiple stages per rank. Uses the backward for weights to fill in
the pipeline bubble.

In particular this is implementing the ZB1P schedule in the paper.

*class*torch.distributed.pipelining.schedules.ScheduleZBVZeroBubble(*stages*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*, *backward_requires_autograd=True*, *defer_pp_recv=False*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L3199)

The Zero Bubble schedule (ZBV variant).
See [https://arxiv.org/pdf/2401.10241](https://arxiv.org/pdf/2401.10241) Section 6 for details.

This schedules requires exactly two stages per rank.

This schedule will perform one forward and one backward on inputs for the microbatches in steady
state and supports multiple stages per rank. Uses backward with respect to weights to fill in
the pipeline bubble.

This ZB-V schedule would have the "zero bubble" property only if time forward == time backward input == time backward weights.
In practice, this is not likely true for real models so alternatively
a greedy scheduler could be implemented for unequal/unbalanced time.

*class*torch.distributed.pipelining.schedules.ScheduleDualPipeV(*stages*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*, *backward_requires_autograd=True*, *defer_pp_recv=False*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L3393)

The DualPipeV schedule. A more efficient schedule variant based on the
DualPipe schedule introduced by DeepSeek in [https://arxiv.org/pdf/2412.19437](https://arxiv.org/pdf/2412.19437)

Based on the open sourced code from [deepseek-ai/DualPipe](https://github.com/deepseek-ai/DualPipe)

*class*torch.distributed.pipelining.schedules.PipelineScheduleSingle(*stage*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *scale_grads=True*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L686)

Base class for single-stage schedules.
Implements the step method.
Derived classes should implement _step_microbatches.

Gradients are scaled by num_microbatches depending on the scale_grads argument, defaulting to True. This setting
should match the configuration of your loss_fn, which may either average losses (scale_grads=True)
or sum losses (scale_grads=False).

step(**args*, *target=None*, *losses=None*, *return_outputs=True*, *loss_kwargs=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L740)

Run one iteration of the pipeline schedule with *whole-batch* input.
Will chunk the input into microbatches automatically, and go through the
microbatches according to the schedule implementation.

args: positional arguments to the model (as in non-pipeline case).
kwargs: keyword arguments to the model (as in non-pipeline case).
target: target for the loss function.
losses: a list to store the losses for each microbatch.
return_outputs: whether to return the outputs from the last stage.
loss_kwargs: extra keyword arguments forwarded to the loss function.

*class*torch.distributed.pipelining.schedules.PipelineScheduleMulti(*stages*, *n_microbatches*, *loss_fn=None*, *args_chunk_spec=None*, *kwargs_chunk_spec=None*, *output_merge_spec=None*, *use_full_backward=None*, *scale_grads=True*, *backward_requires_autograd=True*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L1749)

Base class for multi-stage schedules.
Implements the step method.

Gradients are scaled by num_microbatches depending on the scale_grads argument, defaulting to True. This setting
should match the configuration of your loss_fn, which may either average losses (scale_grads=True)
or sum losses (scale_grads=False).

step(**args*, *target=None*, *losses=None*, *return_outputs=True*, *loss_kwargs=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L1934)

Run one iteration of the pipeline schedule with *whole-batch* input.
Will chunk the input into microbatches automatically, and go through the
microbatches according to the schedule implementation.

args: positional arguments to the model (as in non-pipeline case).
kwargs: keyword arguments to the model (as in non-pipeline case).
target: target for the loss function.
losses: a list to store the losses for each microbatch.
return_outputs: whether to return the outputs from the last stage.
loss_kwargs: extra keyword arguments forwarded to the loss function.

torch.distributed.pipelining.schedules.get_schedule_class(*schedule_name*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/pipelining/schedules.py#L3620)

Maps a schedule name (case insensitive) to its corresponding class object.

Parameters:

**schedule_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the schedule.