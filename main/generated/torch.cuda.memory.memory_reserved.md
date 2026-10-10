# torch.cuda.memory.memory_reserved

torch.cuda.memory.memory_reserved(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/cuda/memory.py#L569)

Return the current GPU memory managed by the caching allocator in bytes for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.