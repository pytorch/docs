# torch.accelerator.memory.reset_accumulated_memory_stats

torch.accelerator.memory.reset_accumulated_memory_stats(*device_index=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/accelerator/memory.py#L198)

Reset the "accumulated" (historical) stats tracked by the current [accelerator](../torch.html#accelerators)
memory allocator for a given device index.

Parameters:

**device_index** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - the index of the device to target.
If not given, use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.
If a [`torch.device`](../tensor_attributes.html#torch.device) or str is provided, its type must match the current
[accelerator](../torch.html#accelerators) device type.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.