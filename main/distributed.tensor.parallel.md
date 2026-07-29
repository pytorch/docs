# Tensor Parallelism - torch.distributed.tensor.parallel

Tensor Parallelism(TP) is built on top of the PyTorch DistributedTensor
([DTensor](https://github.com/pytorch/pytorch/blob/main/torch/distributed/tensor/README.md))
and provides different parallelism styles: Colwise, Rowwise, and Sequence Parallelism.

Warning

Tensor Parallelism APIs are experimental and subject to change.

The entrypoint to parallelize your `nn.Module` using Tensor Parallelism is:

torch.distributed.tensor.parallel.parallelize_module(*module*, *device_mesh=None*, *parallelize_plan=None*, ***, *src_data_rank=0*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/api.py#L14)

Apply Tensor Parallelism in PyTorch by parallelizing modules or sub-modules based on a user-specified plan.

We parallelize module or sub_modules based on a parallelize_plan. The parallelize_plan contains
`ParallelStyle`, which indicates how user wants the module or sub_module
to be parallelized.

User can also specify different parallel style per module fully qualified name (FQN).

Note that `parallelize_module` only accepts a 1-D `DeviceMesh`, if you have a 2-D or N-D `DeviceMesh`,
slice the DeviceMesh to a 1-D sub DeviceMesh first then pass to this API(i.e. `device_mesh["tp"]`)

Parameters:

- **module** (`nn.Module`) - Module to be parallelized.
- **device_mesh** (`DeviceMesh`, optional) - Object which describes the mesh topology of devices for the DTensor.
If not specified, the call must be under a DeviceMesh context.
- **parallelize_plan** (Union[`ParallelStyle`, Dict[str, `ParallelStyle`]], optional) - The plan used to parallelize the module. It can be either a
`ParallelStyle` object which contains how we prepare
input/output for Tensor Parallelism or it can be a dict of module
FQN and its corresponding `ParallelStyle` object. If not
specified, the call will do nothing at the moment.

Keyword Arguments:

**src_data_rank** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the rank of the source data for the logical/global tensor, it is used by
`distribute_tensor()` to scatter/broadcast the shards/replicas to other ranks. By default,
we use `group_rank=0` on each DeviceMesh dimension as the source data to preserve the single-device
semantic. If passing `None` explicitly, `parallelize_module()` simply uses its local data instead
of trying to preserve the single-device semantic via scatter/broadcast. Default: 0

Returns:

A `nn.Module` object parallelized.

Return type:
[*Module*](generated/torch.nn.Module.html#torch.nn.Module)

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, ColwiseParallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>>
>>> # Define the module.
>>> m = Model(...)
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>> m = parallelize_module(m, tp_mesh, {"w1": ColwiseParallel(), "w2": RowwiseParallel()})
>>>
```

Note

For complex module architecture like Attention, MLP layers, we recommend composing
different ParallelStyles together (i.e. `ColwiseParallel` and `RowwiseParallel`) and pass
as a parallelize_plan, to achieve the desired sharding computation.

torch.distributed.tensor.parallel.api.parallelize_module(*module*, *device_mesh=None*, *parallelize_plan=None*, ***, *src_data_rank=0*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/api.py#L14)

Apply Tensor Parallelism in PyTorch by parallelizing modules or sub-modules based on a user-specified plan.

We parallelize module or sub_modules based on a parallelize_plan. The parallelize_plan contains
`ParallelStyle`, which indicates how user wants the module or sub_module
to be parallelized.

User can also specify different parallel style per module fully qualified name (FQN).

Note that `parallelize_module` only accepts a 1-D `DeviceMesh`, if you have a 2-D or N-D `DeviceMesh`,
slice the DeviceMesh to a 1-D sub DeviceMesh first then pass to this API(i.e. `device_mesh["tp"]`)

Parameters:

- **module** (`nn.Module`) - Module to be parallelized.
- **device_mesh** (`DeviceMesh`, optional) - Object which describes the mesh topology of devices for the DTensor.
If not specified, the call must be under a DeviceMesh context.
- **parallelize_plan** (Union[`ParallelStyle`, Dict[str, `ParallelStyle`]], optional) - The plan used to parallelize the module. It can be either a
`ParallelStyle` object which contains how we prepare
input/output for Tensor Parallelism or it can be a dict of module
FQN and its corresponding `ParallelStyle` object. If not
specified, the call will do nothing at the moment.

Keyword Arguments:

**src_data_rank** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the rank of the source data for the logical/global tensor, it is used by
`distribute_tensor()` to scatter/broadcast the shards/replicas to other ranks. By default,
we use `group_rank=0` on each DeviceMesh dimension as the source data to preserve the single-device
semantic. If passing `None` explicitly, `parallelize_module()` simply uses its local data instead
of trying to preserve the single-device semantic via scatter/broadcast. Default: 0

Returns:

A `nn.Module` object parallelized.

Return type:
[*Module*](generated/torch.nn.Module.html#torch.nn.Module)

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, ColwiseParallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>>
>>> # Define the module.
>>> m = Model(...)
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>> m = parallelize_module(m, tp_mesh, {"w1": ColwiseParallel(), "w2": RowwiseParallel()})
>>>
```

Note

For complex module architecture like Attention, MLP layers, we recommend composing
different ParallelStyles together (i.e. `ColwiseParallel` and `RowwiseParallel`) and pass
as a parallelize_plan, to achieve the desired sharding computation.

Tensor Parallelism supports the following parallel styles:

*class*torch.distributed.tensor.parallel.ColwiseParallel(***, *input_layouts=None*, *output_layouts=None*, *use_local_output=True*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/style.py#L45)

Partition a compatible nn.Module in a column-wise fashion. Currently supports nn.Linear and nn.Embedding.
Users can compose it together with RowwiseParallel to achieve the sharding of more complicated modules.
(i.e. MLP, Attention)

Keyword Arguments:

- **input_layouts** ([*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**optional*) - The DTensor layout of input tensor for the nn.Module, this is used to annotate the input tensor to
become a DTensor. If not specified, we assume the input tensor to be replicated.
- **output_layouts** ([*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**optional*) - The DTensor layout of the output for the nn.Module, this is used to ensure the output of the nn.Module
with the user desired layout. If not specified, the output tensor is sharded on the last dimension.
- **use_local_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module output, default: True.

Returns:

A `ParallelStyle` object that represents Colwise sharding of the nn.Module.

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, ColwiseParallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> m = Model(...) # m is a nn.Module that contains a "w1" nn.Linear submodule
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>>
>>> # By default, the input of the "w1" Linear will be converted to Replicated DTensor
>>> # and the output of "w1" will return :class:`torch.Tensor` that shards on the last dim.
>>>
>>> sharded_mod = parallelize_module(m, tp_mesh, {"w1": ColwiseParallel()})
>>> ...
```

Note

By default `ColwiseParallel` output is sharded on the last dimension if the `output_layouts` not
specified, if there're operators that require specific tensor shape (i.e. before the paired `RowwiseParallel`),
keep in mind that if the output is sharded the operator might need to be adjusted to the sharded size.

*class*torch.distributed.tensor.parallel.RowwiseParallel(***, *input_layouts=None*, *output_layouts=None*, *use_local_output=True*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/style.py#L186)

Partition a compatible nn.Module in a row-wise fashion. Currently supports nn.Linear and nn.Embedding.
Users can compose it with ColwiseParallel to achieve the sharding of more complicated modules.
(i.e. MLP, Attention)

Keyword Arguments:

- **input_layouts** ([*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**optional*) - The DTensor layout of input tensor for the nn.Module, this is used to annotate the input tensor to
become a DTensor. If not specified, we assume the input tensor to be sharded on the last dimension.
- **output_layouts** ([*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**optional*) - The DTensor layout of the output for the nn.Module, this is used to ensure the output of the nn.Module
with the user desired layout. If not specified, the output tensor is replicated.
- **use_local_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module output, default: True.

Returns:

A `ParallelStyle` object that represents Rowwise sharding of the nn.Module.

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, RowwiseParallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> m = Model(...) # m is a nn.Module that contains a "w2" nn.Linear submodule
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>>
>>> # By default, the input of the "w2" Linear will be converted to DTensor that shards on the last dim
>>> # and the output of "w2" will return a replicated :class:`torch.Tensor`.
>>>
>>> sharded_mod = parallelize_module(m, tp_mesh, {"w2": RowwiseParallel()}),
>>> ...
```

*class*torch.distributed.tensor.parallel.SequenceParallel(***, *sequence_dim=1*, *use_local_output=False*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/style.py#L339)

SequenceParallel replicates a compatible `nn.Module` parameters and runs the sharded computation with
input sharded on the sequence dimension. This currently supports `nn.LayerNorm`, `nn.Dropout`, and the
[RMSNorm python implementation](https://github.com/facebookresearch/llama/blob/main/llama/model.py#L34)

This style implements the operation that is described in the paper
[Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198)

If the input passed in to this `nn.Module` is a [`torch.Tensor`](tensors.html#torch.Tensor), it assumes that the input is already sharded
on the sequence dimension and converts the input to a `DTensor` sharded on the sequence dimension. If the input
passed in to this `nn.Module` is already a `DTensor` but is not sharded on the sequence dimension, it would
redistribute the input to be sharded on the sequence dimension.

The output of the `nn.Module` will be sharded on the sequence dimension.

Keyword Arguments:

- **sequence_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The sequence dimension of the input tensor for the `nn.Module`, this is used to annotate the input tensor to
become a DTensor that is sharded on the sequence dimension, default: 1.
- **use_local_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module output, default: False.

Returns:

A `ParallelStyle` object that represents Sequence Parallel of the `nn.Module`.

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, SequenceParallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> m = Model(...) # m is a nn.Module that contains a "norm" nn.LayerNorm submodule
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>>
>>> # By default, the input of the "norm" will be converted to DTensor that shards on the sequence dim
>>> # and the output of "norm" will return a sharded on sequence dimension :class:`DTensor`.
>>>
>>> sharded_mod = parallelize_module(m, tp_mesh, {"norm": SequenceParallel()}),
>>> ...
```

Note

SequenceParallel style assumes ones initialization if there are weights in the nn.Module (i.e.
`nn.LayerNorm` or `RMSNorm`, and they by default have ones initialization). If you have custom
inits for the weights on those modules, you need to broadcast the weights before/after parallelizing
to ensure that they are replicated.

To simply configure the nn.Module's inputs and outputs with DTensor layouts
and perform necessary layout redistributions, without distribute the module
parameters to DTensors, the following `ParallelStyle` s can be used in
the `parallelize_plan` when calling `parallelize_module`:

*class*torch.distributed.tensor.parallel.PrepareModuleInput(***, *input_layouts=None*, *desired_input_layouts=None*, *input_kwarg_layouts=None*, *desired_input_kwarg_layouts=None*, *use_local_output=False*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/style.py#L442)

Configure the nn.Module's inputs to convert the input tensors of the nn.Module to DTensors at runtime according to
`input_layouts`, and perform layout redistribution according to the `desired_input_layouts`.

Keyword Arguments:

- **input_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[**Optional**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]**]*) - The DTensor layouts of input tensors for the nn.Module, this is used to convert the input tensors to
DTensors. If some inputs are not torch.Tensor or no need to convert to DTensors, `None` need to be specified
as a placeholder. default: None.
- **desired_input_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[**Optional**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]**]*) - The desired DTensor layout of input tensors for the nn.Module, this is used to ensure the inputs of the nn.Module
have the desired DTensor layouts. This argument needs to have the same length with `input_layouts`. default: None.
- **input_kwarg_layouts** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]*) - The DTensor layouts of input kwargs for the nn.Module, this is used to convert the input kwarg tensors to DTensors.
default: None
- **desired_input_kwarg_layouts** - (Dict[str, Placement]):
The desired DTensor layout of input kwargs for the nn.Module, this is used to ensure the inputs of the nn.Module
have the desired DTensor layouts. default: None.
- **use_local_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module inputs, default: False.

Returns:

A `ParallelStyle` object that prepares the sharding layouts of the nn.Module's inputs.

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, PrepareModuleInput
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> block = TransformerBlock(...) # block is a nn.Module that contains an "attn" Attention submodule
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>>
>>> # According to the style specified below, the first input of attn will be annotated to Sharded DTensor
>>> # and then redistributed to Replicated DTensor.
>>> parallelize_module(
>>> block, # this can be a submodule or module
>>> tp_mesh,
>>> parallelize_plan={
>>> "attn": PrepareModuleInput(
>>> input_layouts=(Shard(0), None, None, ...),
>>> desired_input_layouts=(Replicate(), None, None, ...)
>>> ),
>>> }
>>> )
```

*class*torch.distributed.tensor.parallel.PrepareModuleOutput(***, *output_layouts*, *desired_output_layouts*, *use_local_output=True*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/style.py#L607)

Configure the nn.Module's outputs to convert the output tensors of the nn.Module to DTensors at runtime according to
`output_layouts`, and perform layout redistribution according to the `desired_output_layouts`.

Keyword Arguments:

- **output_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]*) - The DTensor layouts of output tensors for the nn.Module, this is used to convert the output tensors to
DTensors if they are [`torch.Tensor`](tensors.html#torch.Tensor). If some outputs are not torch.Tensor or no need to convert to DTensors,
`None` need to be specified as a placeholder.
- **desired_output_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]*) - The desired DTensor layouts of output tensors for the nn.Module, this is used to ensure the outputs of the nn.Module
have the desired DTensor layouts.
- **use_local_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module outputs, default: True.

Returns:

A ParallelStyle object that prepares the sharding layouts of the nn.Module's outputs.

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, PrepareModuleOutput
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> block = TransformerBlock(...) # block is a nn.Module that contains an "attn" Attention submodule
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>>
>>> # According to the style specified below, the output of the TransformerBlock will be converted to Replicated DTensor
>>> # and then redistributed to Sharded DTensor.
>>> parallelize_module(
>>> block, # this can be a submodule or module
>>> tp_mesh,
>>> parallelize_plan = PrepareModuleOutput(
>>> output_layouts=Replicate(),
>>> desired_output_layouts=Shard(0)
>>> )
>>> )
```

*class*torch.distributed.tensor.parallel.PrepareModuleInputOutput(***, *input_layouts=None*, *desired_input_layouts=None*, *input_kwarg_layouts=None*, *desired_input_kwarg_layouts=None*, *use_local_input=False*, *output_layouts*, *desired_output_layouts*, *use_local_output=True*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/style.py#L717)

Configure the nn.Module's inputs (and outputs) to convert the input tensors (and output tensors, respectively) of the nn.Module
to DTensors at runtime according to `input_layouts` (and output_layouts, respectively), and perform layout redistribution
according to the `desired_input_layouts` (and `desired_output_layouts`, respectively). This is a combination of
`PrepareModuleInput` and `PrepareModuleOutput`.

Keyword Arguments:

- **input_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[**Optional**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]**]*) - The DTensor layouts of input tensors for the nn.Module, this is used to convert the input tensors to
DTensors. If some inputs are not torch.Tensor or no need to convert to DTensors, `None` need to be specified
as a placeholder. default: None.
- **desired_input_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[**Optional**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]**]*) - The desired DTensor layout of input tensors for the nn.Module, this is used to ensure the inputs of the nn.Module
have the desired DTensor layouts. This argument needs to have the same length with `input_layouts`. default: None.
- **input_kwarg_layouts** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]*) - The DTensor layouts of input kwargs for the nn.Module, this is used to convert the input kwarg tensors to DTensors.
default: None
- **desired_input_kwarg_layouts** - (Dict[str, Placement]):
The desired DTensor layout of input kwargs for the nn.Module, this is used to ensure the inputs of the nn.Module
have the desired DTensor layouts. default: None.
- **use_local_input** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module inputs, default: False.
- **output_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]*) - The DTensor layouts of output tensors for the nn.Module, this is used to convert the output tensors to
DTensors if they are [`torch.Tensor`](tensors.html#torch.Tensor). If some outputs are not torch.Tensor or no need to convert to DTensors,
`None` need to be specified as a placeholder.
- **desired_output_layouts** (*Union**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*,**Tuple**[*[*Placement*](distributed.tensor.html#torch.distributed.tensor.placement_types.Placement)*]**]*) - The desired DTensor layouts of output tensors for the nn.Module, this is used to ensure the outputs of the nn.Module
have the desired DTensor layouts.
- **use_local_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to use local [`torch.Tensor`](tensors.html#torch.Tensor) instead of `DTensor` for the module outputs, default: True.

Returns:

A `ParallelStyle` object that prepares the sharding layouts of the nn.Module's inputs and outputs.

Example::

```
>>> from torch.distributed.tensor.parallel import parallelize_module, PrepareModuleInputOutput
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> block = TransformerBlock(...) # block is a nn.Module that contains an "attn" Attention submodule
>>> tp_mesh = init_device_mesh("cuda", (8,))
>>>
>>> # According to the style specified below, the first input of attn will be annotated as Sharded DTensor
>>> # and then redistributed to Replicated DTensor, and the output of the TransformerBlock will be annotated
>>> # as Replicated DTensor and then redistributed to Sharded DTensor.
>>> parallelize_module(
>>> block, # this can be a submodule or module
>>> tp_mesh,
>>> parallelize_plan={
>>> "attn": PrepareModuleInputOutput(
>>> input_layouts=(Shard(0), None, None, ...),
>>> desired_input_layouts=(Replicate(), None, None, ...),
>>> output_layouts=Replicate(),
>>> desired_output_layouts=Shard(0),
>>> ),
>>> }
>>> )
```

Note

when using the `Shard(dim)` as the input/output layouts for the above
`ParallelStyle` s, we assume the input/output activation tensors are evenly sharded on
the tensor dimension `dim` on the `DeviceMesh` that TP operates on. For instance,
since `RowwiseParallel` accepts input that is sharded on the last dimension, it assumes
the input tensor has already been evenly sharded on the last dimension. For the case of uneven sharded activation tensors, one could pass in DTensor directly to the partitioned modules, and use `use_local_output=False` to return DTensor after each `ParallelStyle`, where DTensor could track the uneven sharding information.

For models like Transformer, we recommend users to use `ColwiseParallel`
and `RowwiseParallel` together in the parallelize_plan for achieve the desired
sharding for the entire model (i.e. Attention and MLP).

Parallelized cross-entropy loss computation (loss parallelism), is supported via the following context manager:

torch.distributed.tensor.parallel.loss_parallel()[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/loss.py#L30)

A context manager that enables loss parallelism, where efficient parallelized loss computation
can be performed when the input is sharded on the class dimension. Currently only the cross-entropy
loss is supported.

Within this context manager, one can use [`cross_entropy()`](generated/torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy) or
[`CrossEntropyLoss`](generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) as usual, with the following assumptions on the input parameters.
The corresponding `backward()` call, if any, also needs to happen under this context manager.

Both one-dimensional and multi-dimensional `DeviceMesh` are supported. On a
multi-dimensional mesh, exactly one mesh dim must shard the class dimension --
that dim is treated as the "TP" dim and can be in any position (not necessarily
last). The remaining mesh dims may be `Shard` (e.g. batch-sharded for DP/CP)
or `Replicate`.

Parameters:

- **input** (`DTensor`) - Input logits. Assumed to be sharded on the class dimension on exactly
one mesh dim.
- **target** (Union[[`torch.Tensor`](tensors.html#torch.Tensor), `DTensor`]) -

Must be ground truth class indices (class probabilities currently not
supported). Its placements are derived from `input`'s placements by
(1) replacing the TP dim's `Shard(class_dim)` with `Replicate` and
(2) shifting any other `Shard(d)` with `d > class_dim` down by one
(since the class tensor dim is removed from the output):

```
input tensor shape input placements target shape target placements
---------------------- -------------------------- --------------- ------------------------
(batch, class) (Shard(0), Shard(1)) (batch,) (Shard(0), Replicate())
(batch, class) (Replicate(), Shard(1)) (batch,) (Replicate(), Replicate())
(batch, class, seq) (Shard(2), Shard(1)) (batch, seq) (Shard(1), Replicate())
(batch, class, seq) (Shard(0), Shard(1)) (batch, seq) (Shard(0), Replicate())
```

A plain [`torch.Tensor`](tensors.html#torch.Tensor) is only accepted when the derived target
placements are all `Replicate` (e.g. on a one-dimensional mesh);
otherwise a `DTensor` must be passed explicitly so that the
intended sharding is unambiguous.
- **weight** (Union[[`torch.Tensor`](tensors.html#torch.Tensor), `DTensor`], optional) - If given, assumed to be replicated across the `DeviceMesh`.
- **label_smoothing** - Currently not supported.

Returns:

- `reduction="none"` -- per-sample loss; inherits the `target`
placements (`Shard` on batch-parallel dims, `Replicate` on TP).
- `reduction="sum"` -- scalar; `Replicate` on the TP dim (the custom
all-reduce makes each rank's local value globally correct over TP),
`Partial("sum")` on every other `Shard` mesh dim so that the
cross-rank reduction happens lazily on materialization/redistribution,
and `Replicate` on `Replicate` mesh dims.
- `reduction="mean"` -- only supported on a one-dimensional mesh; returns
a fully replicated `DTensor`.

On a one-dimensional mesh all three cases simplify to a fully replicated
`DTensor` (the original behavior).

Return type:

A `DTensor` whose placements depend on `reduction`

Note

`reduction="mean"` is only supported on a one-dimensional `DeviceMesh`.
On a multi-dimensional mesh the per-rank division by `total_weight` uses a
local count, so aggregating across non-TP dims does not yield the correct
global mean; use `reduction="sum"` or `"none"` instead and divide by the
global count yourself if needed.

Example

A sharded DTensor is manually created here to showcase the usage.
In practice, it is usually the output of a TP module.

```
>>> from torch.distributed.tensor.parallel import loss_parallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> device_mesh = init_device_mesh("cuda", (8,))
>>> input = torch.randn(4, 16, device="cuda", requires_grad=True)
>>> dist_input = distribute_tensor(input, device_mesh, placements=[Shard(1)])
>>> target = torch.randint(16, (4,), device="cuda")
>>> with loss_parallel():
>>> loss = F.cross_entropy(dist_input, target, reduction="mean")
>>> loss.backward()
>>> ...
```

Warning

```
The loss_parallel API is experimental and subject to change.
```

torch.distributed.tensor.parallel.loss.loss_parallel()[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/loss.py#L30)

A context manager that enables loss parallelism, where efficient parallelized loss computation
can be performed when the input is sharded on the class dimension. Currently only the cross-entropy
loss is supported.

Within this context manager, one can use [`cross_entropy()`](generated/torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy) or
[`CrossEntropyLoss`](generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) as usual, with the following assumptions on the input parameters.
The corresponding `backward()` call, if any, also needs to happen under this context manager.

Both one-dimensional and multi-dimensional `DeviceMesh` are supported. On a
multi-dimensional mesh, exactly one mesh dim must shard the class dimension --
that dim is treated as the "TP" dim and can be in any position (not necessarily
last). The remaining mesh dims may be `Shard` (e.g. batch-sharded for DP/CP)
or `Replicate`.

Parameters:

- **input** (`DTensor`) - Input logits. Assumed to be sharded on the class dimension on exactly
one mesh dim.
- **target** (Union[[`torch.Tensor`](tensors.html#torch.Tensor), `DTensor`]) -

Must be ground truth class indices (class probabilities currently not
supported). Its placements are derived from `input`'s placements by
(1) replacing the TP dim's `Shard(class_dim)` with `Replicate` and
(2) shifting any other `Shard(d)` with `d > class_dim` down by one
(since the class tensor dim is removed from the output):

```
input tensor shape input placements target shape target placements
---------------------- -------------------------- --------------- ------------------------
(batch, class) (Shard(0), Shard(1)) (batch,) (Shard(0), Replicate())
(batch, class) (Replicate(), Shard(1)) (batch,) (Replicate(), Replicate())
(batch, class, seq) (Shard(2), Shard(1)) (batch, seq) (Shard(1), Replicate())
(batch, class, seq) (Shard(0), Shard(1)) (batch, seq) (Shard(0), Replicate())
```

A plain [`torch.Tensor`](tensors.html#torch.Tensor) is only accepted when the derived target
placements are all `Replicate` (e.g. on a one-dimensional mesh);
otherwise a `DTensor` must be passed explicitly so that the
intended sharding is unambiguous.
- **weight** (Union[[`torch.Tensor`](tensors.html#torch.Tensor), `DTensor`], optional) - If given, assumed to be replicated across the `DeviceMesh`.
- **label_smoothing** - Currently not supported.

Returns:

- `reduction="none"` -- per-sample loss; inherits the `target`
placements (`Shard` on batch-parallel dims, `Replicate` on TP).
- `reduction="sum"` -- scalar; `Replicate` on the TP dim (the custom
all-reduce makes each rank's local value globally correct over TP),
`Partial("sum")` on every other `Shard` mesh dim so that the
cross-rank reduction happens lazily on materialization/redistribution,
and `Replicate` on `Replicate` mesh dims.
- `reduction="mean"` -- only supported on a one-dimensional mesh; returns
a fully replicated `DTensor`.

On a one-dimensional mesh all three cases simplify to a fully replicated
`DTensor` (the original behavior).

Return type:

A `DTensor` whose placements depend on `reduction`

Note

`reduction="mean"` is only supported on a one-dimensional `DeviceMesh`.
On a multi-dimensional mesh the per-rank division by `total_weight` uses a
local count, so aggregating across non-TP dims does not yield the correct
global mean; use `reduction="sum"` or `"none"` instead and divide by the
global count yourself if needed.

Example

A sharded DTensor is manually created here to showcase the usage.
In practice, it is usually the output of a TP module.

```
>>> from torch.distributed.tensor.parallel import loss_parallel
>>> from torch.distributed.device_mesh import init_device_mesh
>>> ...
>>> device_mesh = init_device_mesh("cuda", (8,))
>>> input = torch.randn(4, 16, device="cuda", requires_grad=True)
>>> dist_input = distribute_tensor(input, device_mesh, placements=[Shard(1)])
>>> target = torch.randint(16, (4,), device="cuda")
>>> with loss_parallel():
>>> loss = F.cross_entropy(dist_input, target, reduction="mean")
>>> loss.backward()
>>> ...
```

torch.distributed.tensor.parallel.input_reshard.input_reshard(*module*, *tp_device_mesh*, *input_reshard_dim=None*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/distributed/tensor/parallel/input_reshard.py#L15)

Register hooks to an nn.Module for input resharding, enabling sharding and restoration during backward computation.

Register hooks to an nn.Module with input resharding so that we can shard
per the given tp_device_mesh and input_reshard_dim and restore the
input back when recomputing the activations in the backward. The reason
why we can do this is that for Tensor Parallel(TP), the input are same
across all TP ranks.

Parameters:

- **module** (`nn.Module`) - Module to be registered with input resharding.
- **tp_device_mesh** (`DeviceMesh`) - Object which describes the mesh topology
of devices for Tensor Parallel.
- **input_reshard_dim** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The dimension of where we perform the sharding
of input. If set None, there is no sharding of input.
Default: None

Returns:

A `nn.Module` object registered with TP input resharding.

Return type:
[*Module*](generated/torch.nn.Module.html#torch.nn.Module)