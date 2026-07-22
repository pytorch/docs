# torch.accelerator.memory.reset_peak_memory_stats

torch.accelerator.memory.reset_peak_memory_stats(*device_index=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/accelerator/memory.py#L217)

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