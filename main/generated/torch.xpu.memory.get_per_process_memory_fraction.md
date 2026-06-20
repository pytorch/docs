# torch.xpu.memory.get_per_process_memory_fraction

torch.xpu.memory.get_per_process_memory_fraction(*device=None*)[[source]](https://github.com/pytorch/pytorch/blob/27b52de22e4e5fa572c07a4065423083a41b8756/torch/xpu/memory.py#L212)

Retrieve the memory fraction currently set for a process on a given XPU device.
This fraction represents the portion of the total device memory that
the caching allocator is allowed to use. The allowed memory is calculated as:

allowed_memory=total_memory×fraction\text{allowed\_memory} = \text{total\_memory} \times \text{fraction}

allowed_memory=total_memory×fraction
Parameters:

**device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - selected device. It uses the current device,
given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device), if `device` is `None` (default).

Returns:

The memory fraction in the range 0.0 to 1.0.

Return type:

[float](https://docs.python.org/3/library/functions.html#float)