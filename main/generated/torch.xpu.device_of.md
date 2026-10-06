# device_of

*class*torch.xpu.device_of(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/xpu/__init__.py#L413)

Context-manager that changes the current device to that of given object.

You can use both tensors and storages as arguments. If a given object is
not allocated on a XPU, this is a no-op.

Parameters:

**obj** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - object allocated on the selected device.