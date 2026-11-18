# torch.cuda.utilization

torch.cuda.utilization(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/5b1433112eb30368cb8f63b3bf0145b391ec72a5/torch/cuda/__init__.py#L1711)

Return the percent of time over the past sample period during which one or
more kernels was executing on the GPU as given by nvidia-smi.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Warning: Each sample period may be between 1 second and 1/6 second,
depending on the product being queried.