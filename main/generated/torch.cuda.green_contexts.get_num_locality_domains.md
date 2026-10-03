# torch.cuda.green_contexts.get_num_locality_domains

torch.cuda.green_contexts.get_num_locality_domains(*device_id=None*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/cuda/green_contexts.py#L115)

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