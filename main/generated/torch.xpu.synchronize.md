# torch.xpu.synchronize

torch.xpu.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/xpu/__init__.py#L645)

Wait for all kernels in all streams on a XPU device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - device for which to synchronize.
It uses the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if [`device`](torch.xpu.device.html#torch.xpu.device) is `None` (default).