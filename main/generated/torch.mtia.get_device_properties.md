# torch.mtia.get_device_properties

torch.mtia.get_device_properties(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/3d5976e3f87222f326a3b2c424828b74ec6cf594/torch/mtia/__init__.py#L285)

Return a dictionary of MTIA device properties

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]