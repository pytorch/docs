# torch.xpu.memory.reset_accumulated_memory_stats

torch.xpu.memory.reset_accumulated_memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/xpu/memory.py#L54)

Reset the "accumulated" (historical) stats tracked by the XPU memory allocator.

See `memory_stats()` for details. Accumulated stats correspond to
the "allocated" and "freed" keys in each individual stat dict.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `device` is `None` (default).