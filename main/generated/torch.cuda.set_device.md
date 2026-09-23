# torch.cuda.set_device

torch.cuda.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/cuda/__init__.py#L751)

Set the current device.

Usage of this function is discouraged in favor of [`device`](torch.cuda.device.html#torch.cuda.device). In most
cases it's better to use `CUDA_VISIBLE_DEVICES` environmental variable.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - selected device. This function is a no-op
if this argument is negative.