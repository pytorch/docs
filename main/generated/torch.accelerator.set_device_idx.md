# torch.accelerator.set_device_idx

torch.accelerator.set_device_idx(*device*, */*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/accelerator/__init__.py#L190)

(Deprecated) Set the current device index to a given device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int) - a given device that must match the current
[accelerator](../torch.html#accelerators) device type.

Warning

`torch.accelerator.set_device_idx()` is deprecated in favor of [`torch.accelerator.set_device_index()`](torch.accelerator.set_device_index.html#torch.accelerator.set_device_index)
and will be removed in a future PyTorch release.