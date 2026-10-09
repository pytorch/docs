# device

*class*torch.mtia.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/mtia/__init__.py#L296)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.