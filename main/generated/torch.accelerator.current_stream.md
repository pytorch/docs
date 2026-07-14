# torch.accelerator.current_stream

torch.accelerator.current_stream(*device=None*, */*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/accelerator/__init__.py#L221)

Return the currently selected stream for a given device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int, optional) - a given device that must match the current
[accelerator](../torch.html#accelerators) device type. If not given,
use [`torch.accelerator.current_device_index()`](torch.accelerator.current_device_index.html#torch.accelerator.current_device_index) by default.

Returns:

the currently selected stream for a given device.

Return type:

[torch.Stream](torch.Stream.html#torch.Stream)