# torch.accelerator.set_device_index

torch.accelerator.set_device_index(*device*, */*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/accelerator/__init__.py#L190)

Set the current device index to a given device.

Parameters:

**device** ([`torch.device`](../tensor_attributes.html#torch.device), str, int) - a given device that must match the current
[accelerator](../torch.html#accelerators) device type.

Note

This function is a no-op if this device index is negative.