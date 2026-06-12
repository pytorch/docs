# torch.cuda.memory.reset_max_memory_cached

torch.cuda.memory.reset_max_memory_cached(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/cuda/memory.py#L506)

Reset the starting point in tracking maximum GPU memory managed by the caching allocator for a given device.

See `max_memory_cached()` for details.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Warning

This function now calls `reset_peak_memory_stats()`, which resets
/all/ peak memory stats.

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.