# torch.mtia.memory.max_memory_allocated

torch.mtia.memory.max_memory_allocated(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/mtia/memory.py#L26)

Return the maximum memory allocated in bytes for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*, or*[*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)