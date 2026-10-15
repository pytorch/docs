# torch.xpu.clock_rate

torch.xpu.clock_rate(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/xpu/__init__.py#L1038)

Return the GPU clock rate in MHz.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float)