# torch.xpu.memory.reset_peak_memory_stats

torch.xpu.memory.reset_peak_memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/xpu/memory.py#L39)

Reset the "peak" stats tracked by the XPU memory allocator.

See `memory_stats()` for details. Peak stats correspond to the
"peak" key in each individual stat dict.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `device` is `None` (default).