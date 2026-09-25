# torch.cuda.memory.memory_summary

torch.cuda.memory.memory_summary(*device=None*, *abbreviated=False*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/cuda/memory.py#L653)

Return a human-readable printout of the current memory allocator statistics for a given device.

This can be useful to display periodically during training, or when
handling out-of-memory exceptions.

Parameters:

- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
printout for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).
- **abbreviated** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - whether to return an abbreviated summary
(default: False).

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

Note

See [Memory management](../notes/cuda.html#cuda-memory-management) for more details about GPU memory
management.