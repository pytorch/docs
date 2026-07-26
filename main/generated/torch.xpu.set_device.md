# torch.xpu.set_device

torch.xpu.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/xpu/__init__.py#L431)

Set the current device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - selected device. This function is a
no-op if this argument is negative.