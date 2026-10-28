# torch.xpu.set_device

torch.xpu.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/7b82415148a0089a719484208bcd61238ed19508/torch/xpu/__init__.py#L457)

Set the current device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - selected device. This function is a
no-op if this argument is negative.