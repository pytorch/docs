# torch.xpu.device_memory_used

torch.xpu.device_memory_used(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/b58511bf7d1e77b23d16cb44e2eacf0f2e05be9c/torch/xpu/__init__.py#L1373)

Return the current GPU used global (device) memory in bytes.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU memory usage information.