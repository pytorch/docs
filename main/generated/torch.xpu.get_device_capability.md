# torch.xpu.get_device_capability

torch.xpu.get_device_capability(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/xpu/__init__.py#L459)

Get the xpu capability of a device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - device for which to
return the device capability. This function is a no-op if this
argument is a negative integer. It uses the current device, given by
[`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device), if [`device`](torch.xpu.device.html#torch.xpu.device) is `None`
(default).

Returns:

the xpu capability dictionary of the device

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Any]