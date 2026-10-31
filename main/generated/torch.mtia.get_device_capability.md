# torch.mtia.get_device_capability

torch.mtia.get_device_capability(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/mtia/__init__.py#L242)

Return capability of a given device as a tuple of (major version, minor version).

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]