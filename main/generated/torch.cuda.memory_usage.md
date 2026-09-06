# torch.cuda.memory_usage

torch.cuda.memory_usage(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/cuda/__init__.py#L1638)

Return the percent of time over the past sample period during which global (device)
memory was being read or written as given by nvidia-smi.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Warning: Each sample period may be between 1 second and 1/6 second,
depending on the product being queried.