# torch.accelerator.memory.memory_reserved

torch.accelerator.memory.memory_reserved(*device_index=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/accelerator/memory.py#L163)

Return the current [accelerator](../torch.html#accelerators) device memory managed by the caching allocator
in bytes for a given device index.

Parameters:

**device_index** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - the index of the device to target.
If not given, use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.
If a [`torch.device`](../tensor_attributes.html#torch.device) or str is provided, its type must match the current
[accelerator](../torch.html#accelerators) device type.

Returns:

the current memory reserved by PyTorch (in bytes) within the current process.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)