# GreenContext

*class*torch.cuda.green_contexts.GreenContext(***, *num_sms=None*, *sm_partition=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L268)

Wrapper around a CUDA green context.

Warning

This API is in beta and may change in future releases.

CUDA work should be placed on streams created from the green context:

```
ctx = GreenContext(...)
stream = ctx.Stream()
with torch.cuda.stream(stream):
 # torch operations here are using resources from `ctx`
 pass
```

Green-context streams are custom CUDA streams. Synchronization with other
streams is the user's responsibility and should be handled with CUDA events,
as with any other custom stream.

Stream()[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L639)

Return a CUDA stream associated with this green context.

Use the returned stream with [`torch.cuda.stream()`](torch.cuda.stream_function.html#torch.cuda.stream) to run work on
the green context. Synchronization with other streams is not automatic;
use CUDA events as with any other custom stream.

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)

*static*create(***, *num_sms=None*, *sm_partition=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L531)

Create a CUDA green context.

Kept for compatibility, see GreenContext constructor.

Return type:

*GreenContext*

*property*device_id*: [int](https://docs.python.org/3/builtins/functions.html#int)*

The device index of this green context.

*static*max_workqueue_concurrency(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L552)

Return the maximum workqueue concurrency limit for the device.

This queries the device for the default number of concurrent
stream-ordered workloads supported by workqueue configuration
resources.

Parameters:

**device_id** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - The device index to query. When
`None`, the current device is used.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

pop_context()[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L612)

Assuming the green context is the current context, pop it from the
context stack and restore the previous context.

Deprecated. Create streams with `Stream()` and use
[`torch.cuda.stream()`](torch.cuda.stream_function.html#torch.cuda.stream) instead.

set_context()[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L583)

Make the green context the current context.

Deprecated. Create streams with `Stream()` and use
[`torch.cuda.stream()`](torch.cuda.stream_function.html#torch.cuda.stream) instead.

*property*sm_count*: [int](https://docs.python.org/3/builtins/functions.html#int)*

The actual number of SMs available to this context.

*property*sm_partition*: [SMPartition](torch.cuda.green_contexts.SMPartition.html#torch.cuda.green_contexts.SMPartition)*

The context's actual SM resource, which can be subdivided.

The returned resource keeps this context alive while it is in use.

*static*split(***, *num_sms=0*, *coscheduled_sm_count=0*, *preferred_coscheduled_sm_count=0*, *backfill=False*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/green_contexts.py#L460)

Create contexts backed by disjoint SM partitions of a device.

Partition options are those of [`SMPartition.split()`](torch.cuda.green_contexts.SMPartition.html#torch.cuda.green_contexts.SMPartition.split). Workqueue
options are applied to each context. Unassigned SMs are unused; use
[`SMPartition.split()`](torch.cuda.green_contexts.SMPartition.html#torch.cuda.green_contexts.SMPartition.split) to retain the remainder for later use.

Example:

```
>>> a, b = GreenContext.split(
... num_sms=(24, 40), coscheduled_sm_count=8, device_id=0
... )
```

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[*GreenContext*, ...]