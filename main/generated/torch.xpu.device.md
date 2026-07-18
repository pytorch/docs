# device

*class*torch.xpu.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/c8080db61856d74ad76795af1c6aa1fd41b7b862/torch/xpu/__init__.py#L396)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.