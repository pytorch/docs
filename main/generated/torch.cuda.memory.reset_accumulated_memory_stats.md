# torch.cuda.memory.reset_accumulated_memory_stats

torch.cuda.memory.reset_accumulated_memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/cuda/memory.py#L362)

Reset the "accumulated" (historical) stats tracked by the CUDA memory allocator.

See `memory_stats()` for details. Accumulated stats correspond to
the "allocated" and "freed" keys in each individual stat dict, as well as
"num_alloc_retries" and "num_ooms".

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.