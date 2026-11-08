# device

*class*torch.cuda.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/__init__.py#L729)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.