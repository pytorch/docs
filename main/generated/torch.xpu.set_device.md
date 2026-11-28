# torch.xpu.set_device

torch.xpu.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/xpu/__init__.py#L470)

Set the current device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - selected device. This function is a
no-op if this argument is negative.