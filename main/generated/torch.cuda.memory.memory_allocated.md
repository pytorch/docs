# torch.cuda.memory.memory_allocated

torch.cuda.memory.memory_allocated(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/cuda/memory.py#L525)

Return the current GPU memory occupied by tensors in bytes for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

Note

This is likely less than the amount shown in nvidia-smi since some
unused memory can be held by the caching allocator and some context
needs to be created on GPU. See [Memory management](../notes/cuda.html#cuda-memory-management) for more
details about GPU memory management.