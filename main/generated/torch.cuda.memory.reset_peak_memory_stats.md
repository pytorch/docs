# torch.cuda.memory.reset_peak_memory_stats

torch.cuda.memory.reset_peak_memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/cuda/memory.py#L381)

Reset the "peak" stats tracked by the CUDA memory allocator.

See `memory_stats()` for details. Peak stats correspond to the
"peak" key in each individual stat dict.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.