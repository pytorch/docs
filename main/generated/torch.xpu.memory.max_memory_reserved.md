# torch.xpu.memory.max_memory_reserved

torch.xpu.memory.max_memory_reserved(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/xpu/memory.py#L180)

Return the maximum GPU memory managed by the caching allocator in bytes for a given device.

By default, this returns the peak cached memory since the beginning of this
program. `reset_peak_memory_stats()` can be used to reset
the starting point in tracking this metric. For example, these two functions
can measure the peak cached memory amount of each iteration in a training
loop.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `device` is `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)