# torch.mtia.get_device_capability

torch.mtia.get_device_capability(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9aee436a1bfc7a0bd2c40f48f128cb185ee3d75e/torch/mtia/__init__.py#L242)

Return capability of a given device as a tuple of (major version, minor version).

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]