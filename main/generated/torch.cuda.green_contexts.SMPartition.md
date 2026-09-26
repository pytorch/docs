# SMPartition

*class*torch.cuda.green_contexts.SMPartition(*_resource*, *_device_id*, *_owner=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L82)

An SM resource selected by CUDA, with its device and allocation metadata.

Obtain resources with `from_device()`, `split()`, or
[`GreenContext.sm_partition`](torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext.sm_partition). Construct a [`GreenContext`](torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext) with
`sm_partition=partition` to run work on the selected SMs.

A partition describes a set of SMs; it does not reserve them against other
contexts. Reusing a partition for multiple contexts shares those SMs.

*property*coscheduled_sm_count*: [int](https://docs.python.org/3/builtins/functions.html#int)*

The co-scheduled SM alignment reported by CUDA for this resource.

*property*device_id*: [int](https://docs.python.org/3/builtins/functions.html#int)*

The device index of this SM resource.

*classmethod*from_device(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L103)

Return the full device SM resource.

Initializes the CUDA driver. If `device_id` is omitted, uses the
current PyTorch device, initializing PyTorch CUDA state if necessary.

Return type:

*SMPartition*

*property*sm_count*: [int](https://docs.python.org/3/builtins/functions.html#int)*

The actual number of SMs in this resource.

split(***, *num_sms=0*, *coscheduled_sm_count=0*, *preferred_coscheduled_sm_count=0*, *backfill=False*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L139)

Split this resource into disjoint groups and an optional remainder.

Requires CUDA driver and bindings 13.1+. CUDA checks the requested
counts and hardware constraints; counts are not automatically rounded.
A count of zero requests discovery of the largest remaining group
satisfying its constraints. Groups are processed in order.

Parameters:

- **num_sms** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or**sequence**of*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - SM count for each group.
Zero requests discovery. Default: `0`.
- **coscheduled_sm_count** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or**sequence**of*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Co-scheduled
SM grouping size for thread-block clusters. Zero lets CUDA
determine cluster capabilities from the selected resources.
Default: `0`.
- **preferred_coscheduled_sm_count** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or**sequence**of*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Preferred larger grouping size, when CUDA can combine groups.
Zero selects the CUDA default. Default: `0`.
- **backfill** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*or**sequence**of*[*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - Allow CUDA to fill
groups with SMs outside complete co-scheduled groupings.
Default: `False`.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[*SMPartition*, ...], *SMPartition* | None]

Each option can be a scalar or a sequence. All sequences must have the
same nonzero length; scalars are broadcast to that length. If every
option is scalar, the split has one group. An early discovery group can
exhaust the SMs needed by later groups.
A group with both `num_sms=0` and `backfill=True` consumes all
remaining SMs and must be the last group.
Returns `(partitions, remainder)`, with `None` for an empty remainder.
The remainder does not inherit the requested alignment.

To subdivide a returned partition or remainder, create a
[`GreenContext`](torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext) from it and split the context's queried
[`sm_partition`](torch.cuda.green_contexts.GreenContext.html#torch.cuda.green_contexts.GreenContext.sm_partition). CUDA drivers can reject raw split
outputs as already partitioned resources. Context creation is explicit.

Children are subsets of this resource and overlap it. Siblings from
this operation, including the remainder, are disjoint. Results from
separate splits on the same or overlapping input resources may overlap.

Example:

```
>>> sms = SMPartition.from_device(device_id=0)
>>> (first,), rest = sms.split(num_sms=4, coscheduled_sm_count=2)
>>> rest_ctx = GreenContext(sm_partition=rest)
>>> (second,), rest = rest_ctx.sm_partition.split(
... num_sms=4, coscheduled_sm_count=2
... )
```