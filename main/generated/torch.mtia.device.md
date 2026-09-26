# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.