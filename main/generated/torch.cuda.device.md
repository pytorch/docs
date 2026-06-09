# device

*class*torch.cuda.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/e3966c93e0ae877c1150f9fceaab6055109ce1c8/torch/cuda/__init__.py#L638)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.