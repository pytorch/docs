# device

*class*torch.cuda.device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/cuda/__init__.py#L716)

Context-manager that changes the selected device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - device index to select. It's a no-op if
this argument is a negative integer or `None`.