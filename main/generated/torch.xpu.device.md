# device

*class*torch.xpu.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/xpu/__init__.py#L389)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.