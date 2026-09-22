# torch.cuda.memory.mem_get_info

torch.cuda.memory.mem_get_info(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/cuda/memory.py#L848)

Return the global free and total GPU memory for a given device using cudaMemGetInfo.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - selected device. Returns
statistic for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default) or if the device index is not specified.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), [int](https://docs.python.org/3/builtins/functions.html#int)]

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more
details about GPU memory management.