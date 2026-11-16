# torch.accelerator.set_device_idx

torch.accelerator.set_device_idx(*device*, */*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/accelerator/__init__.py#L190)

(Deprecated) Set the current device index to a given device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int) - a given device that must match the current
[accelerator](../torch.html#accelerators) device type.

Warning

`torch.accelerator.set_device_idx()` is deprecated in favor of [`torch.accelerator.set_device_index()`](torch.accelerator.set_device_index.html#torch.accelerator.set_device_index)
and will be removed in a future PyTorch release.