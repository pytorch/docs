# torch.cuda.set_device

torch.cuda.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/cuda/__init__.py#L739)

Set the current device.

Usage of this function is discouraged in favor of [`device`](torch.cuda.device.html#torch.cuda.device). In most
cases it's better to use `CUDA_VISIBLE_DEVICES` environmental variable.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - selected device. This function is a no-op
if this argument is negative.