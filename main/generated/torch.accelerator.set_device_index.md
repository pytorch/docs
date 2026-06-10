# torch.accelerator.set_device_index

torch.accelerator.set_device_index(*device*, */*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/accelerator/__init__.py#L188)

Set the current device index to a given device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int) - a given device that must match the current
[accelerator](../torch.html#accelerators) device type.

Note

This function is a no-op if this device index is negative.