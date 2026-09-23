# torch.xpu.get_device_name

torch.xpu.get_device_name(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/xpu/__init__.py#L444)

Get the name of a device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - device for which to
return the name. This function is a no-op if this argument is a
negative integer. It uses the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if [`device`](torch.xpu.device.html#torch.xpu.device) is `None` (default).

Returns:

the name of the device

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)