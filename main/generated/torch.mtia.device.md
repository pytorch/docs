# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.