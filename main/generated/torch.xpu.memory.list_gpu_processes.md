# torch.xpu.memory.list_gpu_processes

torch.xpu.memory.list_gpu_processes(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/9a3243ec510ddea6c63c86d01aef273f400f375f/torch/xpu/memory.py#L625)

Return a printout of running processes and their GPU memory usage on a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - selected device. Uses the
current device, given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device),
if `None` (default).

Returns:

A human-readable summary of each running process and the given GPU memory usage in MB.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

Note

Process status is reported at the physical device level and reflects all processes
associated with the device.