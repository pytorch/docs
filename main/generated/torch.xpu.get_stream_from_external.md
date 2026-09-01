# torch.xpu.get_stream_from_external

torch.xpu.get_stream_from_external(*data_ptr*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/xpu/__init__.py#L668)

Return a [`Stream`](torch.xpu.Stream_class.html#torch.xpu.Stream) from an external SYCL queue.

This function is used to wrap SYCL queue created in other libraries in order
to facilitate data exchange and multi-library interactions.

Note

This function doesn't manage the queue life-cycle, it is the user
responsibility to keep the referenced queue alive while this returned stream is
being used. The different SYCL queue pointers will result in distinct
[`Stream`](torch.xpu.Stream_class.html#torch.xpu.Stream) objects, even if the SYCL queues they dereference are equivalent.

Parameters:

- **data_ptr** ([*int*](https://docs.python.org/3/library/functions.html#int)) - Integer representation of the sycl::queue* value passed externally.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the device where the queue was originally created.
It is the user responsibility to ensure the device is specified correctly.

Return type:

[Stream](torch.xpu.Stream_class.html#torch.xpu.Stream)