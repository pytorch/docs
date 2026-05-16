# torch.cuda.memory.memory_summary

torch.cuda.memory.memory_summary(*device=None*, *abbreviated=False*)[[source]](https://github.com/pytorch/pytorch/blob/df83f06a8c49a667b9408934fa9eaae1aaf32d04/torch/cuda/memory.py#L637)

Return a human-readable printout of the current memory allocator statistics for a given device.

This can be useful to display periodically during training, or when
handling out-of-memory exceptions.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
printout for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).
- **abbreviated** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to return an abbreviated summary
(default: False).

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.