# device_of

*class*torch.cuda.device_of(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/__init__.py#L720)

Context-manager that changes the current device to that of given object.

You can use both tensors and storages as arguments. If a given object is
not allocated on a GPU, this is a no-op.

Parameters:

**obj** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - object allocated on the selected device.