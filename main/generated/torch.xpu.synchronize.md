# torch.xpu.synchronize

torch.xpu.synchronize(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/xpu/__init__.py#L690)

Wait for all kernels in all streams on a XPU device to complete.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - device for which to synchronize.
It uses the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if [`device`](torch.xpu.device.html#torch.xpu.device) is `None` (default).