# Experimental Object Oriented Distributed API

This is an experimental new API for PyTorch Distributed. This is actively in development and subject to change or deletion entirely.

This is intended as a proving ground for more flexible and object oriented distributed APIs.

*class*torch.distributed._dist2.ProcessGroup

Bases: `pybind11_object`

A ProcessGroup is a communication primitive that allows for
collective operations across a group of processes.

This is a base class that provides the interface for all
ProcessGroups. It is not meant to be used directly, but rather
extended by subclasses.

*class*BackendType

Bases: `pybind11_object`

The type of the backend used for the process group.

Members:

> UNDEFINED
> 
> 
> 
> 
> GLOO
> 
> 
> 
> 
> NCCL
> 
> 
> 
> 
> XCCL
> 
> 
> 
> 
> UCC
> 
> 
> 
> 
> MPI
> 
> 
> 
> 
> CUSTOM

CUSTOM*= <BackendType.CUSTOM: 6>*

GLOO*= <BackendType.GLOO: 1>*

MPI*= <BackendType.MPI: 4>*

NCCL*= <BackendType.NCCL: 2>*

UCC*= <BackendType.UCC: 3>*

UNDEFINED*= <BackendType.UNDEFINED: 0>*

XCCL*= <BackendType.XCCL: 5>*

*property*name

*property*value

CUSTOM*= <BackendType.CUSTOM: 6>*

GLOO*= <BackendType.GLOO: 1>*

MPI*= <BackendType.MPI: 4>*

NCCL*= <BackendType.NCCL: 2>*

UCC*= <BackendType.UCC: 3>*

UNDEFINED*= <BackendType.UNDEFINED: 0>*

XCCL*= <BackendType.XCCL: 5>*

abort(*self: torch._C._distributed_c10d.ProcessGroup*) → [None](https://docs.python.org/3/library/constants.html#None)

abort all operations and connections if supported by the backend

all_gather_single(*self: torch._C._distributed_c10d.ProcessGroup*, *output: torch.Tensor*, *input: torch.Tensor*, *opts: torch._C._distributed_c10d.AllgatherOptions = <torch._C._distributed_c10d.AllgatherOptions object at 0x7fa91b868af0>*) → c10d::Work

all_gather_single_coalesced(*self: torch._C._distributed_c10d.ProcessGroup, outputs: collections.abc.Sequence[torch.Tensor], inputs: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllgatherOptions = <torch._C._distributed_c10d.AllgatherOptions object at 0x7fa93e022e30>*) → c10d::Work

Allgathers the input tensors from all processes across the process group.

> See [`torch.distributed.all_gather()`](distributed.html#torch.distributed.all_gather) for more details.

all_to_all_single(**args*, ***kwargs*)

Overloaded function.

1. all_to_all_single(self: torch._C._distributed_c10d.ProcessGroup, output: torch.Tensor, input: torch.Tensor, output_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], input_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], opts: torch._C._distributed_c10d.AllToAllOptions = <torch._C._distributed_c10d.AllToAllOptions object at 0x7fa91b885130>) -> c10d::Work

Alltoalls the input tensors from all processes across the process group.

> See [`torch.distributed.all_to_all_single()`](distributed.html#torch.distributed.all_to_all_single) for more details.

1. all_to_all_single(self: torch._C._distributed_c10d.ProcessGroup, output: torch.Tensor, input: torch.Tensor, output_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], input_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], timeout: datetime.timedelta | None = None) -> c10d::Work

Alltoalls the input tensors from all processes across the process group.

> See [`torch.distributed.all_to_all_single()`](distributed.html#torch.distributed.all_to_all_single) for more details.

allgather(**args*, ***kwargs*)

Overloaded function.

1. allgather(self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[collections.abc.Sequence[torch.Tensor]], input_tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllgatherOptions = <torch._C._distributed_c10d.AllgatherOptions object at 0x7fa91b85dff0>) -> c10d::Work

Allgathers the input tensors from all processes across the process group.

> See [`torch.distributed.all_gather()`](distributed.html#torch.distributed.all_gather) for more details.

1. allgather(self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[torch.Tensor], input_tensor: torch.Tensor, timeout: datetime.timedelta | None = None) -> c10d::Work

Allgathers the input tensors from all processes across the process group.

> See [`torch.distributed.all_gather()`](distributed.html#torch.distributed.all_gather) for more details.

allgather_coalesced(*self: torch._C._distributed_c10d.ProcessGroup, output_lists: collections.abc.Sequence[collections.abc.Sequence[torch.Tensor]], input_list: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllgatherOptions = <torch._C._distributed_c10d.AllgatherOptions object at 0x7fa91b87c970>*) → c10d::Work

Allgathers the input tensors from all processes across the process group.

> See [`torch.distributed.all_gather()`](distributed.html#torch.distributed.all_gather) for more details.

allgather_into_tensor_coalesced(*self: torch._C._distributed_c10d.ProcessGroup, outputs: collections.abc.Sequence[torch.Tensor], inputs: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllgatherOptions = <torch._C._distributed_c10d.AllgatherOptions object at 0x7fa91b890cf0>*) → c10d::Work

Allgathers the input tensors from all processes across the process group.

> See [`torch.distributed.all_gather()`](distributed.html#torch.distributed.all_gather) for more details.

allreduce(**args*, ***kwargs*)

Overloaded function.

1. allreduce(self: torch._C._distributed_c10d.ProcessGroup, tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllreduceOptions = <torch._C._distributed_c10d.AllreduceOptions object at 0x7fa91b84feb0>) -> c10d::Work

Allreduces the provided tensors across all processes in the process group.

> See [`torch.distributed.all_reduce()`](distributed.html#torch.distributed.all_reduce) for more details.

1. allreduce(self: torch._C._distributed_c10d.ProcessGroup, tensors: collections.abc.Sequence[torch.Tensor], op: torch._C._distributed_c10d.ReduceOp = <RedOpType.SUM: 0>, timeout: datetime.timedelta | None = None) -> c10d::Work

Allreduces the provided tensors across all processes in the process group.

> See [`torch.distributed.all_reduce()`](distributed.html#torch.distributed.all_reduce) for more details.

1. allreduce(self: torch._C._distributed_c10d.ProcessGroup, tensor: torch.Tensor, op: torch._C._distributed_c10d.ReduceOp = <RedOpType.SUM: 0>, timeout: datetime.timedelta | None = None) -> c10d::Work

Allreduces the provided tensors across all processes in the process group.

> See [`torch.distributed.all_reduce()`](distributed.html#torch.distributed.all_reduce) for more details.

allreduce_coalesced(*self: torch._C._distributed_c10d.ProcessGroup, tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllreduceCoalescedOptions = <torch._C._distributed_c10d.AllreduceCoalescedOptions object at 0x7fa942d90430>*) → c10d::Work

Allreduces the provided tensors across all processes in the process group.

> See [`torch.distributed.all_reduce()`](distributed.html#torch.distributed.all_reduce) for more details.

alltoall(*self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[torch.Tensor], input_tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.AllToAllOptions = <torch._C._distributed_c10d.AllToAllOptions object at 0x7fa91b8919f0>*) → c10d::Work

Alltoalls the input tensors from all processes across the process group.

> See [`torch.distributed.all_to_all()`](distributed.html#torch.distributed.all_to_all) for more details.

alltoall_base(**args*, ***kwargs*)

Overloaded function.

1. alltoall_base(self: torch._C._distributed_c10d.ProcessGroup, output: torch.Tensor, input: torch.Tensor, output_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], input_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], opts: torch._C._distributed_c10d.AllToAllOptions = <torch._C._distributed_c10d.AllToAllOptions object at 0x7fa91b891770>) -> c10d::Work

Alltoalls the input tensors from all processes across the process group.

> See [`torch.distributed.all_to_all()`](distributed.html#torch.distributed.all_to_all) for more details.

1. alltoall_base(self: torch._C._distributed_c10d.ProcessGroup, output: torch.Tensor, input: torch.Tensor, output_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], input_split_sizes: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], timeout: datetime.timedelta | None = None) -> c10d::Work

Alltoalls the input tensors from all processes across the process group.

> See [`torch.distributed.all_to_all()`](distributed.html#torch.distributed.all_to_all) for more details.

barrier(**args*, ***kwargs*)

Overloaded function.

1. barrier(self: torch._C._distributed_c10d.ProcessGroup, opts: torch._C._distributed_c10d.BarrierOptions = <torch._C._distributed_c10d.BarrierOptions object at 0x7fa91b891d70>) -> c10d::Work

Blocks until all processes in the group enter the call, and

then all leave the call together.

See [`torch.distributed.barrier()`](distributed.html#torch.distributed.barrier) for more details.

1. barrier(self: torch._C._distributed_c10d.ProcessGroup, timeout: datetime.timedelta | None = None) -> c10d::Work

Blocks until all processes in the group enter the call, and

then all leave the call together.

See [`torch.distributed.barrier()`](distributed.html#torch.distributed.barrier) for more details.

*property*bound_device_id

boxed(*self: torch._C._distributed_c10d.ProcessGroup*) → [object](https://docs.python.org/3/library/functions.html#object)

broadcast(**args*, ***kwargs*)

Overloaded function.

1. broadcast(self: torch._C._distributed_c10d.ProcessGroup, tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.BroadcastOptions = <torch._C._distributed_c10d.BroadcastOptions object at 0x7fa91b887cb0>) -> c10d::Work

Broadcasts the tensor to all processes in the process group.

> See [`torch.distributed.broadcast()`](distributed.html#torch.distributed.broadcast) for more details.

1. broadcast(self: torch._C._distributed_c10d.ProcessGroup, tensor: torch.Tensor, root: typing.SupportsInt | typing.SupportsIndex, timeout: datetime.timedelta | None = None) -> c10d::Work

Broadcasts the tensor to all processes in the process group.

> See [`torch.distributed.broadcast()`](distributed.html#torch.distributed.broadcast) for more details.

gather(**args*, ***kwargs*)

Overloaded function.

1. gather(self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[collections.abc.Sequence[torch.Tensor]], input_tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.GatherOptions = <torch._C._distributed_c10d.GatherOptions object at 0x7fa91b868db0>) -> c10d::Work

Gathers the input tensors from all processes across the process group.

> See [`torch.distributed.gather()`](distributed.html#torch.distributed.gather) for more details.

1. gather(self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[torch.Tensor], input_tensor: torch.Tensor, root: typing.SupportsInt | typing.SupportsIndex, timeout: datetime.timedelta | None = None) -> c10d::Work

Gathers the input tensors from all processes across the process group.

> See [`torch.distributed.gather()`](distributed.html#torch.distributed.gather) for more details.

get_backend(*self: [object](https://docs.python.org/3/library/functions.html#object)*, *device: [torch.device](tensor_attributes.html#torch.device)*) → [object](https://docs.python.org/3/library/functions.html#object)

Return the underlying backend implementation for this process group and device.

This API bypasses torch.compile tracing and other hooks. Backend methods are
experimental and subject to breakage without warning.

get_group_store(*self: torch._C._distributed_c10d.ProcessGroup*) → torch._C._distributed_c10d.Store

Get the store of this process group.

get_reconfigure_handle(*self: torch._C._distributed_c10d.ProcessGroup*) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Get an opaque reconfigure handle used to (re)initialize peers for fault tolerance

*property*group_desc

Gets this process group description

*property*group_name

(Gets this process group name. It's cluster unique)

merge_remote_group(*self: torch._C._distributed_c10d.ProcessGroup*, *store: torch._C._distributed_c10d.Store*, *size: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*, *timeout: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta) = datetime.timedelta(seconds=1800)*, *group_name: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *group_desc: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None*) → torch._C._distributed_c10d.ProcessGroup

monitored_barrier(*self: torch._C._distributed_c10d.ProcessGroup*, *timeout: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta) | [None](https://docs.python.org/3/library/constants.html#None) = None*, *wait_all_ranks: [bool](https://docs.python.org/3/library/functions.html#bool) = False*) → [None](https://docs.python.org/3/library/constants.html#None)

Blocks until all processes in the group enter the call, and

then all leave the call together.

See [`torch.distributed.monitored_barrier()`](distributed.html#torch.distributed.monitored_barrier) for more details.

name(*self: torch._C._distributed_c10d.ProcessGroup*) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Get the name of this process group.

new_window(*self: torch._C._distributed_c10d.ProcessGroup*, *tensor: [torch.Tensor](tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None) = None*) → torch._C._distributed_c10d.Window

Create a new one-sided communication window

rank(*self: torch._C._distributed_c10d.ProcessGroup*) → [int](https://docs.python.org/3/library/functions.html#int)

Get the rank of this process group.

reconfigure(*self: torch._C._distributed_c10d.ProcessGroup*, *opts: torch._C._distributed_c10d.ReconfigureOptions*) → c10d::Work

Reconfigure the process group with a new set of peers for fault tolerance

recv(*self: torch._C._distributed_c10d.ProcessGroup*, *tensors: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[torch.Tensor](tensors.html#torch.Tensor)]*, *srcRank: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*, *tag: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → c10d::Work

Receives the tensor from the specified rank.

> See [`torch.distributed.recv()`](distributed.html#torch.distributed.recv) for more details.

recv_anysource(*self: torch._C._distributed_c10d.ProcessGroup*, *arg0: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[torch.Tensor](tensors.html#torch.Tensor)]*, *arg1: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → c10d::Work

Receives the tensor from any source.

> See [`torch.distributed.recv()`](distributed.html#torch.distributed.recv) for more details.

reduce(**args*, ***kwargs*)

Overloaded function.

1. reduce(self: torch._C._distributed_c10d.ProcessGroup, tensors: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.ReduceOptions = <torch._C._distributed_c10d.ReduceOptions object at 0x7fa91b8905f0>) -> c10d::Work

Reduces the provided tensors across all processes in the process group.

> See [`torch.distributed.reduce()`](distributed.html#torch.distributed.reduce) for more details.

1. reduce(self: torch._C._distributed_c10d.ProcessGroup, tensor: torch.Tensor, root: typing.SupportsInt | typing.SupportsIndex, op: torch._C._distributed_c10d.ReduceOp = <RedOpType.SUM: 0>, timeout: datetime.timedelta | None = None) -> c10d::Work

Reduces the provided tensors across all processes in the process group.

> See [`torch.distributed.reduce()`](distributed.html#torch.distributed.reduce) for more details.

reduce_scatter(**args*, ***kwargs*)

Overloaded function.

1. reduce_scatter(self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[torch.Tensor], input_tensors: collections.abc.Sequence[collections.abc.Sequence[torch.Tensor]], opts: torch._C._distributed_c10d.ReduceScatterOptions = <torch._C._distributed_c10d.ReduceScatterOptions object at 0x7fa93e034a30>) -> c10d::Work

Reduces and scatters the input tensors from all processes across the process group.

> See [`torch.distributed.reduce_scatter()`](distributed.html#torch.distributed.reduce_scatter) for more details.

1. reduce_scatter(self: torch._C._distributed_c10d.ProcessGroup, output: torch.Tensor, input: collections.abc.Sequence[torch.Tensor], op: torch._C._distributed_c10d.ReduceOp = <RedOpType.SUM: 0>, timeout: datetime.timedelta | None = None) -> c10d::Work

Reduces and scatters the input tensors from all processes across the process group.

> See [`torch.distributed.reduce_scatter()`](distributed.html#torch.distributed.reduce_scatter) for more details.

reduce_scatter_single(*self: torch._C._distributed_c10d.ProcessGroup*, *outputTensor: torch.Tensor*, *inputTensor: torch.Tensor*, *opts: torch._C._distributed_c10d.ReduceScatterOptions = <torch._C._distributed_c10d.ReduceScatterOptions object at 0x7fa91b87f130>*) → c10d::Work

reduce_scatter_single_coalesced(*self: torch._C._distributed_c10d.ProcessGroup, outputs: collections.abc.Sequence[torch.Tensor], inputs: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.ReduceScatterOptions = <torch._C._distributed_c10d.ReduceScatterOptions object at 0x7fa91b885070>*) → c10d::Work

Reduces and scatters the input tensors from all processes across the process group.

> See [`torch.distributed.reduce_scatter()`](distributed.html#torch.distributed.reduce_scatter) for more details.

reduce_scatter_tensor_coalesced(*self: torch._C._distributed_c10d.ProcessGroup, outputs: collections.abc.Sequence[torch.Tensor], inputs: collections.abc.Sequence[torch.Tensor], opts: torch._C._distributed_c10d.ReduceScatterOptions = <torch._C._distributed_c10d.ReduceScatterOptions object at 0x7fa91b885030>*) → c10d::Work

Reduces and scatters the input tensors from all processes across the process group.

> See [`torch.distributed.reduce_scatter()`](distributed.html#torch.distributed.reduce_scatter) for more details.

register_abort_hook(*self: torch._C._distributed_c10d.ProcessGroup*, *hook_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*, *hook: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], [None](https://docs.python.org/3/library/constants.html#None)]*) → [None](https://docs.python.org/3/library/constants.html#None)

Register an abort hook, called before abort on timeout/error

register_post_hook(*self: torch._C._distributed_c10d.ProcessGroup*, *hook_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*, *hook: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[torch._C._distributed_c10d.PostHookArgs], [None](https://docs.python.org/3/library/constants.html#None)]*) → [None](https://docs.python.org/3/library/constants.html#None)

Register a post-hook, called after each collective is issued

register_pre_hook(*self: torch._C._distributed_c10d.ProcessGroup*, *hook_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*, *hook: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[torch._C._distributed_c10d.PreHookArgs], [None](https://docs.python.org/3/library/constants.html#None)]*) → [None](https://docs.python.org/3/library/constants.html#None)

Register a pre-hook, called before each collective is issued

scatter(**args*, ***kwargs*)

Overloaded function.

1. scatter(self: torch._C._distributed_c10d.ProcessGroup, output_tensors: collections.abc.Sequence[torch.Tensor], input_tensors: collections.abc.Sequence[collections.abc.Sequence[torch.Tensor]], opts: torch._C._distributed_c10d.ScatterOptions = <torch._C._distributed_c10d.ScatterOptions object at 0x7fa91b890f30>) -> c10d::Work

Scatters the input tensors from all processes across the process group.

> See [`torch.distributed.scatter()`](distributed.html#torch.distributed.scatter) for more details.

1. scatter(self: torch._C._distributed_c10d.ProcessGroup, output_tensor: torch.Tensor, input_tensors: collections.abc.Sequence[torch.Tensor], root: typing.SupportsInt | typing.SupportsIndex, timeout: datetime.timedelta | None = None) -> c10d::Work

Scatters the input tensors from all processes across the process group.

> See [`torch.distributed.scatter()`](distributed.html#torch.distributed.scatter) for more details.

send(*self: torch._C._distributed_c10d.ProcessGroup*, *tensors: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[torch.Tensor](tensors.html#torch.Tensor)]*, *dstRank: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*, *tag: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → c10d::Work

Sends the tensor to the specified rank.

> See [`torch.distributed.send()`](distributed.html#torch.distributed.send) for more details.

set_timeout(*self: torch._C._distributed_c10d.ProcessGroup*, *timeout: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta)*) → [None](https://docs.python.org/3/library/constants.html#None)

Sets the default timeout for all future operations.

shutdown(*self: torch._C._distributed_c10d.ProcessGroup*) → [None](https://docs.python.org/3/library/constants.html#None)

shutdown the process group

size(*self: torch._C._distributed_c10d.ProcessGroup*) → [int](https://docs.python.org/3/library/functions.html#int)

Get the size of this process group.

split_group(*self: torch._C._distributed_c10d.ProcessGroup, ranks: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], timeout: datetime.timedelta | None = None, opts: c10d::Backend::Options | None = None, group_name: str | None = None, group_desc: str | None = None, device_types: collections.abc.Sequence[torch.device] | None = None*) → torch._C._distributed_c10d.ProcessGroup

*property*supports_reconfigure

(test whether the process group supports reconfigure for fault tolerance)

*property*supports_window

(test whether the process group supports one-sided window operations)

*static*unbox(*arg0: [object](https://docs.python.org/3/library/functions.html#object)*) → torch._C._distributed_c10d.ProcessGroup

unregister_abort_hook(*self: torch._C._distributed_c10d.ProcessGroup*, *hook_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → [None](https://docs.python.org/3/library/constants.html#None)

unregister_post_hook(*self: torch._C._distributed_c10d.ProcessGroup*, *hook_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → [None](https://docs.python.org/3/library/constants.html#None)

unregister_pre_hook(*self: torch._C._distributed_c10d.ProcessGroup*, *hook_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → [None](https://docs.python.org/3/library/constants.html#None)

*property*use_pg_for_symm_mem_rendezvous

*class*torch.distributed._dist2.ProcessGroupFactory(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/distributed/_dist2.py#L36)

Bases: [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

Protocol for process group factories.

torch.distributed._dist2.current_process_group()[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/distributed/_dist2.py#L188)

Get the current process group. Thread local method.

Returns:

The current process group.

Return type:

*ProcessGroup*

torch.distributed._dist2.new_group(*backend*, *timeout*, *device*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/distributed/_dist2.py#L156)

Create a new process group with the given backend and options. This group is
independent and will not be globally registered and thus not usable via the
standard torch.distributed.* APIs.

Parameters:

- **backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The backend to use for the process group.
- **timeout** ([*timedelta*](https://docs.python.org/3/library/datetime.html#datetime.timedelta)) - The timeout for collective operations.
- **device** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*device*](tensor_attributes.html#torch.device)) - The device to use for the process group.
- ****kwargs** ([*object*](https://docs.python.org/3/library/functions.html#object)) - All remaining arguments are passed to the backend constructor.
See the backend specific documentation for details.

Returns:

A new process group.

Return type:

*ProcessGroup*

torch.distributed._dist2.process_group(*pg*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/distributed/_dist2.py#L198)

Context manager for process groups. Thread local method.

Parameters:

**pg** (*ProcessGroup*) - The process group to use.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]

torch.distributed._dist2.register_backend(*name*, *func*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/distributed/_dist2.py#L50)

Register a new process group backend.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The name of the backend.
- **func** (*ProcessGroupFactory*) - The function to create the process group.