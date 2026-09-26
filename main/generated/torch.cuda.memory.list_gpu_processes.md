# torch.cuda.memory.list_gpu_processes

torch.cuda.memory.list_gpu_processes(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/cuda/memory.py#L782)

Return a human-readable printout of the running processes and their GPU memory use for a given device.

This can be useful to display periodically during training, or when
handling out-of-memory exceptions.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Returns
printout for the current device, given by [`current_device()`](torch.cuda.current_device.html#torch.cuda.current_device),
if `device` is `None` (default).

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)