# torch.xpu.memory.list_gpu_processes

torch.xpu.memory.list_gpu_processes(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/xpu/memory.py#L627)

Return a printout of running processes and their GPU memory usage on a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Returns:

A human-readable summary of each running process and the given GPU memory usage in MB.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

Note

Process status is reported at the physical device level and reflects all processes
associated with the device.