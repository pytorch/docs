# torch.cuda.memory.max_memory_reserved

torch.cuda.memory.max_memory_reserved(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/516f64b797cf7645a973e20d856d3e0ddec79948/torch/cuda/memory.py#L586)

Return the maximum GPU memory managed by the caching allocator in bytes for a given device.

By default, this returns the peak cached memory since the beginning of this
program. `reset_peak_memory_stats()` can be used to reset
the starting point in tracking this metric. For example, these two functions
can measure the peak cached memory amount of each iteration in a training
loop.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.