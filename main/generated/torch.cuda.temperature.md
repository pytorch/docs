# torch.cuda.temperature

torch.cuda.temperature(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/cuda/__init__.py#L1613)

Return the average temperature of the GPU sensor in Degrees C (Centigrades).

The average temperature is computed based on past sample period as given by nvidia-smi.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Warning: Each sample period may be between 1 second and 1/6 second,
depending on the product being queried.