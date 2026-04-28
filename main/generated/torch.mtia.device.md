# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/4ff2d1161191378e895e560774c1622dba40076d/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.