# torch.xpu.temperature

torch.xpu.temperature(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/__init__.py#L946)

Return the GPU temperature in degrees Celsius.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU temperature information.