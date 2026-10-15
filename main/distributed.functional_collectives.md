# Functional Collectives

Functional collectives return new tensors instead of mutating their inputs and
are traceable by `torch.compile`. In eager mode the result is an
`AsyncCollectiveTensor` which waits on the collective on first use.

Functional collectives take the group as an argument. Under `torch.compile` they are traced into the graph so the compiler can reorder and overlap communication.

Note

The [`torch.distributed.nn.functional`](distributed.html#module-torch.distributed.nn.functional) module is deprecated in favor of this module.

```
import torch.distributed as dist
import torch.distributed.functional_collectives as funcol

# group can be a ProcessGroup, DeviceMesh, (DeviceMesh, dim) or group name.
out = funcol.all_reduce(tensor, "sum", group=dist.group.WORLD)
gathered = funcol.all_gather_single(tensor, gather_dim=0, group=mesh)
```

torch.distributed.functional_collectives.all_reduce(*self*, *reduceOp*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L170)

Reduces the tensor data across all machines in such a way that all get
the final result.

The input tensor is left unmodified.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

:: N.B. `premul_sum` backward assumes the pre-multiplier is identical on
every rank. With a per-rank (or tensor) factor the backward is incorrect: it
re-applies `premul_sum` to the gradient, yielding `sum_s k_s * g_s`,
instead of scaling the summed gradient locally by this rank's `k_r`.

torch.distributed.functional_collectives.all_reduce_coalesced(*self*, *reduceOp*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L423)

Reduces a list of tensors across all machines in such a way that all get
the final result.

The all tensors in the input list are left unmodified.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

:: N.B. `premul_sum` backward assumes the pre-multiplier is identical on
every rank. With a per-rank (or tensor) factor the backward is incorrect: it
re-applies `premul_sum` to the gradient, yielding `sum_s k_s * g_s`,
instead of scaling the summed gradient locally by this rank's `k_r`.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[*Tensor*](tensors.html#torch.Tensor)]

torch.distributed.functional_collectives.all_gather_single(*self*, *gather_dim*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L210)

Gather tensor data across from all machines and concatenate over `gather_dim`.

The input tensor is left unmodified.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

torch.distributed.functional_collectives.all_gather_single_coalesced(*self*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L463)

Gather a list of tensors across from all machines.

Note that it currently only supports gather_dim = 0.

The input tensor is left unmodified.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[*Tensor*](tensors.html#torch.Tensor)]

torch.distributed.functional_collectives.reduce_scatter_single(*self*, *reduceOp*, *scatter_dim*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L278)

Reduces the tensor data across all machines in such a way that all get
the final result, then scatter the results to corresponding ranks.

The input tensor is left unmodified.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

torch.distributed.functional_collectives.reduce_scatter_single_coalesced(*inputs*, *reduceOp*, *scatter_dim*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L494)

Reduces a list of tensors across all machines in such a way that all get
the final result, then scatter the results to corresponding ranks.

The input tensors are left unmodified.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[*Tensor*](tensors.html#torch.Tensor)]

torch.distributed.functional_collectives.all_to_all_single(*self*, *output_split_sizes*, *input_split_sizes*, *group*, *tag=''*, ***, *config=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L597)

Each process splits input tensor and then scatters the split list
to all processes in a group. Then concatenate the received tensors from all
the processes in the group and return single output tensor.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

:: N.B. If you pass a PG or a 1D list to perform a MPMD collective, the compiler won't be able to recover
that information and perform collective algebraic optimization. Use other forms of input for that.

Return type:

[*Tensor*](tensors.html#torch.Tensor)

torch.distributed.functional_collectives.broadcast(*self*, *src*, *group*, *tag=''*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L154)

Broadcasts the tensor to all processes in the given process group.

Parameters:

- **src** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - Source rank
- **group** (*ProcessGroup**or**List**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]*) - The process group to work on.
- **tag** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - A unique identifier for the collective. Default: empty string

torch.distributed.functional_collectives.permute_tensor(*self*, *src_dst*, *group*, *tag=''*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L1208)

Permutes the elements of the tensor according to the given source/destination pairs. src_dst should
be defined such that src_dst[m] == n means m sends to n.

Group can be one of:

List[int]: ranks participating in the collective.
List[List[int]]: 2D mesh of ranks taking part of this collective in MPMD.
ProcessGroup: Will perform a collective using the ranks and tag of the PG.
DeviceMesh: Do a SPMD collective over all ranks of the mesh
(DeviceMesh, int): Do a MPMD collective over one dimension of the DeviceMesh

Return type:

[*Tensor*](tensors.html#torch.Tensor)

torch.distributed.functional_collectives.wait_tensor(*tensor*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L138)

Wait on a tensor returned by the collectives ops.

Waiting follows device semantics, which means blocking on CPU and synchronizing streams on CUDA.

torch.distributed.functional_collectives.wait_tensors(*tensors*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L147)

Wait on tensors returned by the same multi-output collective.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[*Tensor*](tensors.html#torch.Tensor)]

*class*torch.distributed.functional_collectives.AsyncCollectiveTensor(*elem*)

A Tensor wrapper subclass that is used to trigger a call to wait
prior to first use of the underlying tensor.
Use it inside functional collective pytorch wrappers like the following:

```
def functional_collective(self, group, tag):
 group_name = _resolve_group(group, tag)
 tensor = torch.ops._c10d_functional.{collective}(self, ..., group_name)
 return _maybe_wrap_tensor(tensor)
```

numpy()[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L1355)

Wait on the collective and return the result as a NumPy array.

tolist()[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L1275)

Wait on the collective and return the result as a list.

trigger_wait()[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L1299)

Wait on the collective if not yet completed and return the result tensor.

wait()[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/distributed/_functional_collectives.py#L1308)

Wait on the collective and return the result tensor.

Return type:

[*Tensor*](tensors.html#torch.Tensor)