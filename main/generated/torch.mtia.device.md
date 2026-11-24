# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.