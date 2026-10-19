# device_of

*class*torch.xpu.device_of(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/xpu/__init__.py#L442)

Context-manager that changes the current device to that of given object.

You can use both tensors and storages as arguments. If a given object is
not allocated on a XPU, this is a no-op.

Parameters:

**obj** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - object allocated on the selected device.