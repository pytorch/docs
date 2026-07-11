# torch.cuda.memory_usage

torch.cuda.memory_usage(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e708521bdf92712674ed3a0d332b56c356502328/torch/cuda/__init__.py#L1567)

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