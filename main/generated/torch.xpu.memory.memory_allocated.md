# torch.xpu.memory.memory_allocated

torch.xpu.memory.memory_allocated(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/xpu/memory.py#L133)

Return the current GPU memory occupied by tensors in bytes for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `device` is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Note

This is likely less than the amount shown in xpu-smi since some
unused memory can be held by the caching allocator and some context
needs to be created on GPU.