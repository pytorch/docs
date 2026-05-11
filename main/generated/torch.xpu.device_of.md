# device_of

*class*torch.xpu.device_of(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/xpu/__init__.py#L409)

Context-manager that changes the current device to that of given object.

You can use both tensors and storages as arguments. If a given object is
not allocated on a XPU, this is a no-op.

Parameters:

**obj** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - object allocated on the selected device.