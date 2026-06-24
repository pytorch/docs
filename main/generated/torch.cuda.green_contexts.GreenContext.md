# GreenContext

*class*torch.cuda.green_contexts.GreenContext(***, *num_sms=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/cuda/green_contexts.py#L74)

Wrapper around a CUDA green context.

Warning

This API is in beta and may change in future releases.

Stream()[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/cuda/green_contexts.py#L334)

Return the CUDA Stream used by the green context.

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)

*static*create(***, *num_sms=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/cuda/green_contexts.py#L237)

Create a CUDA green context.

Kept for compatibility, see GreenContext constructor.

Return type:

*GreenContext*

*static*max_workqueue_concurrency(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/cuda/green_contexts.py#L256)

Return the maximum workqueue concurrency limit for the device.

This queries the device for the default number of concurrent
stream-ordered workloads supported by workqueue configuration
resources.

Parameters:

**device_id** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device index to query. When
`None`, the current device is used.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

pop_context()[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/cuda/green_contexts.py#L311)

Assuming the green context is the current context, pop it from the
context stack and restore the previous context.

set_context()[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/cuda/green_contexts.py#L287)

Make the green context the current context.