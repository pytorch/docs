# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.