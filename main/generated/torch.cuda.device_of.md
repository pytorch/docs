# device_of

*class*torch.cuda.device_of(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/__init__.py#L736)

Context-manager that changes the current device to that of given object.

You can use both tensors and storages as arguments. If a given object is
not allocated on a GPU, this is a no-op.

Parameters:

**obj** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - object allocated on the selected device.