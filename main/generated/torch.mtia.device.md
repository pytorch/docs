# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/40a42e9b743c053cc9e6d11c0502026a8f5d7d57/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.