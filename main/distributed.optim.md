# Distributed Optimizers

Warning

Distributed optimizer is not currently supported when using CUDA tensors

`torch.distributed.optim` exposes DistributedOptimizer, which takes a list
of remote parameters (`RRef`) and runs the
optimizer locally on the workers where the parameters live. The distributed
optimizer can use any of the local optimizer [Base class](optim.html#optimizer-algorithms) to
apply the gradients on each worker.

*class*torch.distributed.optim.DistributedOptimizer(*optimizer_class*, *params_rref*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/optimizer.py#L127)

DistributedOptimizer takes remote references to parameters scattered
across workers and applies the given optimizer locally for each parameter.

This class uses [`get_gradients()`](rpc.html#torch.distributed.autograd.get_gradients) in order
to retrieve the gradients for specific parameters.

Concurrent calls to
`step()`,
either from the same or different clients, will
be serialized on each worker - as each worker's optimizer can only work
on one set of gradients at a time. However, there is no guarantee that
the full forward-backward-optimizer sequence will execute for one client
at a time. This means that the gradients being applied may not correspond
to the latest forward pass executed on a given worker. Also, there is no
guaranteed ordering across workers.

DistributedOptimizer creates the local optimizer with TorchScript enabled
by default, so that optimizer updates are not blocked by the Python Global
Interpreter Lock (GIL) in the case of multithreaded training (e.g. Distributed
Model Parallel). This feature is currently enabled for most optimizers. You
can also follow [the recipe](https://github.com/pytorch/tutorials/pull/1465) in PyTorch tutorials to enable TorchScript support
for your own custom optimizers.

Parameters:

- **optimizer_class** ([*optim.Optimizer*](optim.html#torch.optim.Optimizer)) - the class of optimizer to
instantiate on each worker.
- **params_rref** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**RRef**]*) - list of RRefs to local or remote parameters
to optimize.
- **args** - arguments to pass to the optimizer constructor on each worker.
- **kwargs** - arguments to pass to the optimizer constructor on each worker.

Example::

```
>>> import torch.distributed.autograd as dist_autograd
>>> import torch.distributed.rpc as rpc
>>> from torch import optim
>>> from torch.distributed.optim import DistributedOptimizer
>>>
>>> with dist_autograd.context() as context_id:
>>> # Forward pass.
>>> rref1 = rpc.remote("worker1", torch.add, args=(torch.ones(2), 3))
>>> rref2 = rpc.remote("worker1", torch.add, args=(torch.ones(2), 1))
>>> loss = rref1.to_here() + rref2.to_here()
>>>
>>> # Backward pass.
>>> dist_autograd.backward(context_id, [loss.sum()])
>>>
>>> # Optimizer.
>>> dist_optim = DistributedOptimizer(
>>> optim.SGD,
>>> [rref1, rref2],
>>> lr=0.05,
>>> )
>>> dist_optim.step(context_id)
```

step(*context_id*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/optimizer.py#L224)

Performs a single optimization step.

This will call [`torch.optim.Optimizer.step()`](generated/torch.optim.Optimizer.step.html#torch.optim.Optimizer.step) on each worker
containing parameters to be optimized, and will block until all workers
return. The provided `context_id` will be used to retrieve the
corresponding [`context`](rpc.html#torch.distributed.autograd.context) that
contains the gradients that should be applied to the parameters.

Parameters:

**context_id** - the autograd context id for which we should run the
optimizer step.

*class*torch.distributed.optim.PostLocalSGDOptimizer(*optim*, *averager*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/post_localSGD_optimizer.py#L8)

Wraps an arbitrary [`torch.optim.Optimizer`](optim.html#torch.optim.Optimizer) and runs [post-local SGD](https://arxiv.org/abs/1808.07217),
This optimizer runs local optimizer at every step.
After the warm-up stage, it averages parameters periodically after the local optimizer is applied.

Parameters:

- **optim** ([*Optimizer*](optim.html#torch.optim.Optimizer)) - The local optimizer.
- **averager** (*ModelAverager*) - A model averager instance to run post-localSGD algorithm.

Example:

```
>>> import torch
>>> import torch.distributed as dist
>>> import torch.distributed.algorithms.model_averaging.averagers as averagers
>>> import torch.nn as nn
>>> from torch.distributed.optim import PostLocalSGDOptimizer
>>> from torch.distributed.algorithms.ddp_comm_hooks.post_localSGD_hook import (
>>> PostLocalSGDState,
>>> post_localSGD_hook,
>>> )
>>>
>>> model = nn.parallel.DistributedDataParallel(
>>> module, device_ids=[rank], output_device=rank
>>> )
>>>
>>> # Register a post-localSGD communication hook.
>>> state = PostLocalSGDState(process_group=None, subgroup=None, start_localSGD_iter=100)
>>> model.register_comm_hook(state, post_localSGD_hook)
>>>
>>> # Create a post-localSGD optimizer that wraps a local optimizer.
>>> # Note that ``warmup_steps`` used in ``PostLocalSGDOptimizer`` must be the same as
>>> # ``start_localSGD_iter`` used in ``PostLocalSGDState``.
>>> local_optim = torch.optim.SGD(params=model.parameters(), lr=0.01)
>>> opt = PostLocalSGDOptimizer(
>>> optim=local_optim,
>>> averager=averagers.PeriodicModelAverager(period=4, warmup_steps=100)
>>> )
>>>
>>> # In the first 100 steps, DDP runs global gradient averaging at every step.
>>> # After 100 steps, DDP runs gradient averaging within each subgroup (intra-node by default),
>>> # and post-localSGD optimizer runs global model averaging every 4 steps after applying the local optimizer.
>>> for step in range(0, 200):
>>> opt.zero_grad()
>>> loss = loss_fn(output, labels)
>>> loss.backward()
>>> opt.step()
```

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/post_localSGD_optimizer.py#L80)

This is the same as [`torch.optim.Optimizer`](optim.html#torch.optim.Optimizer) `load_state_dict()`,
but also restores model averager's step value to the one
saved in the provided `state_dict`.

If there is no `"step"` entry in `state_dict`,
it will raise a warning and initialize the model averager's step to 0.

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/post_localSGD_optimizer.py#L70)

This is the same as [`torch.optim.Optimizer`](optim.html#torch.optim.Optimizer) `state_dict()`,
but adds an extra entry to record model averager's step to the checkpoint
to ensure reload does not cause unnecessary warm up again.

step()[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/post_localSGD_optimizer.py#L100)

Performs a single optimization step (parameter update).

*class*torch.distributed.optim.ZeroRedundancyOptimizer(*params*, *optimizer_class*, *process_group=None*, *parameters_as_bucket_view=False*, *overlap_with_ddp=False*, ***defaults*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L290)

Wrap an arbitrary [`optim.Optimizer`](optim.html#torch.optim.Optimizer) and shards its states across ranks in the group.

The sharing is done as described by [ZeRO](https://arxiv.org/abs/1910.02054).

The local optimizer instance in each rank is only
responsible for updating approximately `1 / world_size` parameters and
hence only needs to keep `1 / world_size` optimizer states. After
parameters are updated locally, each rank will broadcast its parameters to
all other peers to keep all model replicas in the same state.
`ZeroRedundancyOptimizer` can be used in conjunction with
[`torch.nn.parallel.DistributedDataParallel`](generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel) to reduce per-rank peak
memory consumption.

`ZeroRedundancyOptimizer` uses a sorted-greedy algorithm to pack a number
of parameters at each rank. Each parameter belongs to a single rank and is
not divided among ranks. The partition is arbitrary and might not match the
the parameter registration or usage order.

Parameters:

**params** (`Iterable`) - an `Iterable` of [`torch.Tensor`](tensors.html#torch.Tensor) s
or [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) s giving all parameters, which will be sharded
across ranks.

Keyword Arguments:

- **optimizer_class** (`torch.nn.Optimizer`) - the class of the local
optimizer.
- **process_group** (`ProcessGroup`, optional) - `torch.distributed`
`ProcessGroup` (default: `dist.group.WORLD` initialized by
[`torch.distributed.init_process_group()`](distributed.html#torch.distributed.init_process_group)).
- **parameters_as_bucket_view** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, parameters are
packed into buckets to speed up communication, and `param.data`
fields point to bucket views at different offsets; if `False`,
each individual parameter is communicated separately, and each
`params.data` stays intact (default: `False`).
- **overlap_with_ddp** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if `True`, `step()` is
overlapped with `DistributedDataParallel` 's gradient
synchronization; this requires (1) either a functional optimizer
for the `optimizer_class` argument or one with a functional
equivalent and (2) registering a DDP communication hook
constructed from one of the functions in `ddp_zero_hook.py`;
parameters are packed into buckets matching those in
`DistributedDataParallel`, meaning that the
`parameters_as_bucket_view` argument is ignored.
If `False`, `step()` runs disjointly after the backward pass
(per normal).
(default: `False`)
- ****defaults** - any trailing arguments, which are forwarded to the local
optimizer.

Example:

```
>>> import torch.nn as nn
>>> from torch.distributed.optim import ZeroRedundancyOptimizer
>>> from torch.nn.parallel import DistributedDataParallel as DDP
>>> model = nn.Sequential(*[nn.Linear(2000, 2000).to(rank) for _ in range(20)])
>>> ddp = DDP(model, device_ids=[rank])
>>> opt = ZeroRedundancyOptimizer(
>>> ddp.parameters(),
>>> optimizer_class=torch.optim.Adam,
>>> lr=0.01
>>> )
>>> ddp(inputs).sum().backward()
>>> opt.step()
```

Warning

Currently, `ZeroRedundancyOptimizer` requires that all of the
passed-in parameters are the same dense type.

Warning

If you pass `overlap_with_ddp=True`, be wary of the following: Given
the way that overlapping `DistributedDataParallel` with
`ZeroRedundancyOptimizer` is currently implemented, the first
two or three training iterations do not perform parameter updates in
the optimizer step, depending on if `static_graph=False` or
`static_graph=True`, respectively. This is because it needs
information about the gradient bucketing strategy used by
`DistributedDataParallel`, which is not finalized until the
second forward pass if `static_graph=False` or until the third
forward pass if `static_graph=True`. To adjust for this, one option
is to prepend dummy inputs.

Warning

ZeroRedundancyOptimizer is experimental and subject to change.

add_param_group(*param_group*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L467)

Add a parameter group to the `Optimizer` 's `param_groups`.

This can be useful when fine tuning a pre-trained network, as frozen
layers can be made trainable and added to the `Optimizer` as
training progresses.

Parameters:

**param_group** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - specifies the parameters to be optimized and
group-specific optimization options.

Warning

This method handles updating the shards on all partitions
but needs to be called on all ranks. Calling this on a subset of
the ranks will cause the training to hang because communication
primitives are called depending on the managed parameters and
expect all the ranks to participate on the same set of parameters.

consolidate_state_dict(*to=0*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L513)

Consolidate a list of `state_dict` s (one per rank) on the target rank.

Parameters:

**to** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the rank that receives the optimizer states (default: 0).

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if `overlap_with_ddp=True` and this method is
 called before this `ZeroRedundancyOptimizer` instance
 has been fully initialized, which happens once
 `DistributedDataParallel` gradient buckets have been
 rebuilt.

Warning

This needs to be called on all ranks.

*property*join_device*: [device](tensor_attributes.html#torch.device)*

Return default device.

join_hook(***_kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L1155)

Return the ZeRO join hook.

It enables training on uneven inputs by
shadowing the collective communications in the optimizer step.

Gradients must be properly set before this hook is called.

Parameters:

**kwargs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) containing any keyword arguments
to modify the behavior of the join hook at run time; all
`Joinable` instances sharing the same join context
manager are forwarded the same value for `kwargs`.

Return type:

[*JoinHook*](distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook)

This hook does not support any keyword arguments; i.e. `kwargs` is
unused.

*property*join_process_group*: [Any](https://docs.python.org/3/library/typing.html#typing.Any)*

Return process group.

load_state_dict(*state_dict*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L1185)

Load the state pertaining to the given rank from the input `state_dict`, updating the local optimizer as needed.

Parameters:

**state_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) - optimizer state; should be an object returned
from a call to `state_dict()`.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if `overlap_with_ddp=True` and this method is
 called before this `ZeroRedundancyOptimizer` instance
 has been fully initialized, which happens once
 `DistributedDataParallel` gradient buckets have been
 rebuilt.

state_dict()[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L1223)

Return the last global optimizer state known to this rank.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if `overlap_with_ddp=True` and this method is
 called before this `ZeroRedundancyOptimizer` instance
 has been fully initialized, which happens once
 `DistributedDataParallel` gradient buckets have been
 rebuilt; or if this method is called without a preceding call
 to `consolidate_state_dict()`.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

step(*closure=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/7e49a76253edc1ab706e08750fcdacd6cfc5e114/torch/distributed/optim/zero_redundancy_optimizer.py#L1124)

Perform a single optimizer step and syncs parameters across all ranks.

Parameters:

**closure** (*Callable*) - a closure that re-evaluates the model and
returns the loss; optional for most optimizers.

Returns:

Optional loss depending on the underlying local optimizer.

Return type:

[float](https://docs.python.org/3/library/functions.html#float) | None

Note

Any extra parameters are passed to the base optimizer as-is.