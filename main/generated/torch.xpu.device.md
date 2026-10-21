# device

*class*torch.xpu.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/1404563568be4b2d23634a409bd7a9c7972c1c5c/torch/xpu/__init__.py#L422)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.