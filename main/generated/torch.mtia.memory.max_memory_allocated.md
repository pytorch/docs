# torch.mtia.memory.max_memory_allocated

torch.mtia.memory.max_memory_allocated(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/mtia/memory.py#L26)

Return the maximum memory allocated in bytes for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*, or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)