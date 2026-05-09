# GreenContext

*class*torch.cuda.green_contexts.GreenContext[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/cuda/green_contexts.py#L18)

Wrapper around a CUDA green context.

Warning

This API is in beta and may change in future releases.

Stream()[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/cuda/green_contexts.py#L90)

Return the CUDA Stream used by the green context.

Return type:

[*Stream*](torch.cuda.streams.Stream.html#torch.cuda.streams.Stream)

*static*create(***, *num_sms=None*, *workqueue_scope=None*, *workqueue_concurrency_limit=None*, *device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/cuda/green_contexts.py#L25)

Create a CUDA green context.

At least one of `num_sms` or `workqueue_scope` must be specified.
Both can be combined to partition SMs and configure workqueues in the
same green context.

Parameters:

- **num_sms** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The number of SMs to use in the green
context. When `None`, SMs are not partitioned.
- **workqueue_scope** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - Workqueue sharing scope. One of
`"device_ctx"` (shared across all contexts, default driver
behaviour) or `"balanced"` (non-overlapping workqueues with
other balanced green contexts). When `None`, no workqueue
configuration is applied.
- **workqueue_concurrency_limit** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Maximum number of
concurrent stream-ordered workloads for the workqueue. Requires
`workqueue_scope` to be set.
- **device_id** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device index of green context.
When `None`, the current device is used.

Return type:

[object](https://docs.python.org/3/library/functions.html#object)

*static*max_workqueue_concurrency(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/cuda/green_contexts.py#L62)

Return the maximum workqueue concurrency limit for the device.

This queries the device for the default number of concurrent
stream-ordered workloads supported by workqueue configuration
resources.

Parameters:

**device_id** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The device index to query. When
`None`, the current device is used.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

pop_context()[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/cuda/green_contexts.py#L84)

Assuming the green context is the current context, pop it from the
context stack and restore the previous context.

set_context()[[source]](https://github.com/pytorch/pytorch/blob/b14e6fb508b03fc0a98fefe9b0750ba0d63500da/torch/cuda/green_contexts.py#L80)

Make the green context the current context.