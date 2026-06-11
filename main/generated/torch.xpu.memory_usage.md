# torch.xpu.memory_usage

torch.xpu.memory_usage(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/xpu/__init__.py#L1244)

Return the GPU memory bandwidth usage as a percentage.

The value is computed by dividing the byte-transfer delta by the time delta
between two bandwidth-counter reads separated by a 100ms sampling interval,
then normalizing by the peak bandwidth reported by the hardware.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

Note

This function blocks for approximately 100ms per call due to the
sampling interval required to compute an accurate bandwidth reading.

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU memory bandwidth usage information.