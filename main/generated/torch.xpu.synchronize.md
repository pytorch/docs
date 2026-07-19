# torch.xpu.synchronize

torch.xpu.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c69ee1f95bf01999272fb9964a85290e019ec24d/torch/xpu/__init__.py#L693)

Wait for all kernels in all streams on a XPU device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - device for which to synchronize.
It uses the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if [`device`](torch.xpu.device.html#torch.xpu.device) is `None` (default).