# torch.mtia.get_device_capability

torch.mtia.get_device_capability(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/mtia/__init__.py#L242)

Return capability of a given device as a tuple of (major version, minor version).

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]