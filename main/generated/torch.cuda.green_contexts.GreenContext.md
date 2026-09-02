# GreenContext

*class*torch.cuda.green_contexts.GreenContext(***, *num_sms=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/green_contexts.py#L81)

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

Stream()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/green_contexts.py#L364)

Return a CUDA stream associated with this green context.

Use the returned stream with [`torch.cuda.stream()`](torch.cuda.stream_function.html#torch.cuda.stream) to run work on
the green context. Synchronization with other streams is not automatic;
use CUDA events as with any other custom stream.

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)

*static*create(***, *num_sms=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/green_contexts.py#L258)

Create a CUDA green context.

Kept for compatibility, see GreenContext constructor.

Return type:

*GreenContext*

*static*max_workqueue_concurrency(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/green_contexts.py#L277)

Return the maximum workqueue concurrency limit for the device.

This queries the device for the default number of concurrent
stream-ordered workloads supported by workqueue configuration
resources.

Parameters:

**device_id** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device index to query. When
`None`, the current device is used.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

pop_context()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/green_contexts.py#L337)

Assuming the green context is the current context, pop it from the
context stack and restore the previous context.

Deprecated. Create streams with `Stream()` and use
[`torch.cuda.stream()`](torch.cuda.stream_function.html#torch.cuda.stream) instead.

set_context()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/green_contexts.py#L308)

Make the green context the current context.

Deprecated. Create streams with `Stream()` and use
[`torch.cuda.stream()`](torch.cuda.stream_function.html#torch.cuda.stream) instead.