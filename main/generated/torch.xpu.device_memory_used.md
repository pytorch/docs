# torch.xpu.device_memory_used

torch.xpu.device_memory_used(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/xpu/__init__.py#L1407)

Return the current GPU used global (device) memory in bytes.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU memory usage information.