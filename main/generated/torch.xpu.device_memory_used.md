# torch.xpu.device_memory_used

torch.xpu.device_memory_used(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/xpu/__init__.py#L1291)

Return the current GPU used global (device) memory in bytes.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU memory usage information.