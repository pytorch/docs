# torch.xpu.clock_rate

torch.xpu.clock_rate(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/xpu/__init__.py#L979)

Return the GPU clock rate in MHz.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[float](https://docs.python.org/3/library/functions.html#float)