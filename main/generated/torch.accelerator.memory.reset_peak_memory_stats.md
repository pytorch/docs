# torch.accelerator.memory.reset_peak_memory_stats

torch.accelerator.memory.reset_peak_memory_stats(*device_index=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/accelerator/memory.py#L219)

Reset the "peak" stats tracked by the current [accelerator](../torch.html#accelerators)
memory allocator for a given device index.

Parameters:

**device_index** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - the index of the device to target.
If not given, use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.
If a [`torch.device`](../tensor_attributes.html#torch.device) or str is provided, its type must match the current
[accelerator](../torch.html#accelerators) device type.

Note

This function is a no-op if the memory allocator for the current
[accelerator](../torch.html#accelerators) has not been initialized.