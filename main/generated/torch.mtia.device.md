# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.