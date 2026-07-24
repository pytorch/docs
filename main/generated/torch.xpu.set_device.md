# torch.xpu.set_device

torch.xpu.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/xpu/__init__.py#L431)

Set the current device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - selected device. This function is a
no-op if this argument is negative.