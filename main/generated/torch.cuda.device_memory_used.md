# torch.cuda.device_memory_used

torch.cuda.device_memory_used(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/cuda/__init__.py#L1511)

Return used global (device) memory in bytes as given by nvidia-smi or amd-smi.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if [`device`](torch.cuda.device.html#torch.cuda.device) is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)