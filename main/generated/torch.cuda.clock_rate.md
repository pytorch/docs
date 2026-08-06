# torch.cuda.clock_rate

torch.cuda.clock_rate(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/eaa2ebb41a524b2e9d0d3223864d2f48ab132992/torch/cuda/__init__.py#L1705)

Return the clock speed of the GPU SM in MHz (megahertz) over the past sample period as given by nvidia-smi.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Warning: Each sample period may be between 1 second and 1/6 second,
depending on the product being queried.