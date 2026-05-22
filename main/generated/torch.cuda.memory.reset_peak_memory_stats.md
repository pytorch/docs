# torch.cuda.memory.reset_peak_memory_stats

torch.cuda.memory.reset_peak_memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/cuda/memory.py#L380)

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