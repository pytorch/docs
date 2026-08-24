# device

*class*torch.cuda.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/9bc1ff884cb38c4f6485d73c20a922b782335b34/torch/cuda/__init__.py#L716)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.