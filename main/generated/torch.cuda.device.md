# device

*class*torch.cuda.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/5f228673c58f6d36691c0cbc5c677fdf0c349372/torch/cuda/__init__.py#L733)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.