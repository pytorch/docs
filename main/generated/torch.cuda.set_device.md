# torch.cuda.set_device

torch.cuda.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/__init__.py#L764)

Set the current device.

Usage of this function is discouraged in favor of [`device`](torch.cuda.device.html#torch.cuda.device). In most
cases it's better to use `CUDA_VISIBLE_DEVICES` environmental variable.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - selected device. This function is a no-op
if this argument is negative.