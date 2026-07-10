# torch.cuda.set_device

torch.cuda.set_device(*device*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/cuda/__init__.py#L735)

Set the current device.

Usage of this function is discouraged in favor of [`device`](torch.cuda.device.html#torch.cuda.device). In most
cases it's better to use `CUDA_VISIBLE_DEVICES` environmental variable.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - selected device. This function is a no-op
if this argument is negative.