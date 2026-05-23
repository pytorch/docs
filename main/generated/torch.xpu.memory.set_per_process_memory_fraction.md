# torch.xpu.memory.set_per_process_memory_fraction

torch.xpu.memory.set_per_process_memory_fraction(*fraction*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/xpu/memory.py#L232)

Set the memory fraction for a single process on XPU device.
This function limits the amount of memory that the caching allocator can allocate
on the specified XPU device. The allowed memory is computed as:

allowed_memory=total_memory×fraction\text{allowed\_memory} = \text{total\_memory} \times \text{fraction}

allowed_memory=total_memory×fraction

If the process attempts to allocate more than this allowed memory,
an out-of-memory error will be raised by the allocator.

Parameters:

- **fraction** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Range: 0~1. Allowed memory equals total_memory * fraction.
- **device** ([*torch.device*](../tensor_attributes.html#torch.device)*or*[*int*](https://docs.python.org/3/library/functions.html#int)*or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - selected device. It uses the current device,
given by [`current_device()`](torch.xpu.current_device.html#torch.xpu.current_device), if `device` is `None` (default).

Note

In general, the total available free memory is less than the total capacity.