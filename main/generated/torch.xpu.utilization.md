# torch.xpu.utilization

torch.xpu.utilization(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/xpu/__init__.py#L1192)

Return the GPU engine utilization as a percentage.

The value is computed by dividing the active-time delta by the time delta
between two engine-activity reads separated by a 100ms sampling interval.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

Note

This function blocks for approximately 100ms per call due to the
sampling interval required to compute an accurate utilization reading.

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU utilization information.