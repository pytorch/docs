# torch.accelerator.set_device_index

torch.accelerator.set_device_index(*device*, */*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/accelerator/__init__.py#L189)

Set the current device index to a given device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int) - a given device that must match the current
[accelerator](../torch.html#accelerators) device type.

Note

This function is a no-op if this device index is negative.