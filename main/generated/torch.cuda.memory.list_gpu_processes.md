# torch.cuda.memory.list_gpu_processes

torch.cuda.memory.list_gpu_processes(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/df83f06a8c49a667b9408934fa9eaae1aaf32d04/torch/cuda/memory.py#L766)

Return a human-readable printout of the running processes and their GPU memory use for a given device.

This can be useful to display periodically during training, or when
handling out-of-memory exceptions.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Returns
printout for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)