# torch.xpu.device_memory_used

torch.xpu.device_memory_used(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/xpu/__init__.py#L1293)

Return the current GPU used global (device) memory in bytes.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU memory usage information.