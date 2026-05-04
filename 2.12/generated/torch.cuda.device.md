# device

*class*torch.cuda.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/v2.12.0/torch/cuda/__init__.py#L604)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.