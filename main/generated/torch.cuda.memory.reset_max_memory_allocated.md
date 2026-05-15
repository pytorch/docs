# torch.cuda.memory.reset_max_memory_allocated

torch.cuda.memory.reset_max_memory_allocated(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/cuda/memory.py#L465)

Reset the starting point in tracking maximum GPU memory occupied by tensors for a given device.

See `max_memory_allocated()` for details.

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