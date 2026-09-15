# torch.cuda.power_draw

torch.cuda.power_draw(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/cuda/__init__.py#L1701)

Return the average power draw of the GPU sensor in mW (MilliWatts)

over the past sample period as given by nvidia-smi for Fermi or newer fully supported devices.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Warning: Each sample period may be between 1 second and 1/6 second,
depending on the product being queried.