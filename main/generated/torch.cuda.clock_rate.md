# torch.cuda.clock_rate

torch.cuda.clock_rate(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/__init__.py#L1761)

Return the clock speed of the GPU SM in MHz (megahertz) over the past sample period as given by nvidia-smi.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Warning: Each sample period may be between 1 second and 1/6 second,
depending on the product being queried.