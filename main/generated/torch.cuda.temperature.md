# torch.cuda.temperature

torch.cuda.temperature(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/__init__.py#L1674)

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