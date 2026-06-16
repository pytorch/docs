# torch.accelerator.memory.memory_allocated

torch.accelerator.memory.memory_allocated(*device_index=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/accelerator/memory.py#L126)

Return the current [accelerator](../torch.html#accelerators) device memory occupied by tensors
in bytes for a given device index.

Parameters:

**device_index** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - the index of the device to target.
If not given, use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.
If a [`torch.device`](../tensor_attributes.html#torch.device) or str is provided, its type must match the current
[accelerator](../torch.html#accelerators) device type.

Returns:

the current memory occupied by live tensors (in bytes) within the current process.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)