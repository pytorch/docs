# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.