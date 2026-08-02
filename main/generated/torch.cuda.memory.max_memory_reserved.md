# torch.cuda.memory.max_memory_reserved

torch.cuda.memory.max_memory_reserved(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/30731ee8f01763cf1d32dc2e3962f51fc034c482/torch/cuda/memory.py#L578)

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

Note

Under `PYTORCH_CUDA_ALLOC_CONF=backend:cudaMallocAsync`, the peak is
computed by summing the high-water marks of the default mempool and the
device graph-memory pool (CUDA graph captures reserve backing in the
latter). Because those two high-water marks need not occur at the same
instant, the reported peak is a conservative *upper bound* on the true
simultaneous peak. The current value
(`memory_reserved()`) is exact.