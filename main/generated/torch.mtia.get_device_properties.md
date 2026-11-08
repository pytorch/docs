# torch.mtia.get_device_properties

torch.mtia.get_device_properties(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/mtia/__init__.py#L285)

Return a dictionary of MTIA device properties

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]