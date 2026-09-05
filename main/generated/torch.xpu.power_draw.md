# torch.xpu.power_draw

torch.xpu.power_draw(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/13818df097cc56c9a2a860678049f2a42a008853/torch/xpu/__init__.py#L1088)

Return the GPU card power draw in watts.

The value is computed by dividing the energy delta by the time delta between
two energy-counter reads separated by a 100ms sampling interval.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[float](https://docs.python.org/3/library/functions.html#float)

Note

This function blocks for approximately 100ms per call due to the
sampling interval required to compute an accurate power reading.

Note

This API may require elevated privileges (e.g. `sudo`) to access GPU power information.

Note

On Intel Xe2 and newer GPUs, card-level power is reported directly. On older GPUs,
package-level power is used as a fallback and may not reflect the full card power draw.