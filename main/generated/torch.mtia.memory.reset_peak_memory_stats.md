# torch.mtia.memory.reset_peak_memory_stats

torch.mtia.memory.reset_peak_memory_stats(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/mtia/memory.py#L52)

Reset the peak memory stats for a given device.

Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*,*[*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*, or*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - statistics for the current device, given by current_device(),
if device is None (default).