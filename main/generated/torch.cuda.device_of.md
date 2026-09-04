# device_of

*class*torch.cuda.device_of(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/cuda/__init__.py#L736)

Context-manager that changes the current device to that of given object.

You can use both tensors and storages as arguments. If a given object is
not allocated on a GPU, this is a no-op.

Parameters:

**obj** ([*Tensor*](../tensors.html#torch.Tensor)*or**Storage*) - object allocated on the selected device.