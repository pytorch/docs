# torch.nn.functional.fold

torch.nn.functional.fold(*input*, *output_size*, *kernel_size*, *dilation=1*, *padding=0*, *stride=1*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/nn/functional.py#L6188)

Combine an array of sliding local blocks into a large containing tensor.

Warning

Currently, only unbatched (3D) or batched (4D) image-like output tensors are supported.

See [`torch.nn.Fold`](torch.nn.Fold.html#torch.nn.Fold) for details

Return type:

[*Tensor*](../tensors.html#torch.Tensor)