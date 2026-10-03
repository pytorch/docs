# torch.xpu.device_memory_used

torch.xpu.device_memory_used(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/xpu/__init__.py#L1370)

Return the current GPU used global (device) memory in bytes.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU memory usage information.