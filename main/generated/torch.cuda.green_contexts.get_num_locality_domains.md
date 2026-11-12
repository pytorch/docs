# torch.cuda.green_contexts.get_num_locality_domains

torch.cuda.green_contexts.get_num_locality_domains(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/cuda/green_contexts.py#L115)

Return the device's locality-domain count reported by CUDA.

Returns `1` when the required software is unavailable. With CUDA driver
and bindings 13.4+, initializes the CUDA driver and queries the count.
This query does not create a context when `device_id` is specified;
invalid devices and failed driver queries raise an error.
Initializing the driver can prevent CUDA use in subsequently forked children.

Parameters:

**device_id** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - Device index. When `None`, uses the current
PyTorch device, initializing PyTorch CUDA state if necessary.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)