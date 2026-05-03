# torch.nn.functional.fold

torch.nn.functional.fold(*input*, *output_size*, *kernel_size*, *dilation=1*, *padding=0*, *stride=1*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/nn/functional.py#L5947)

Combine an array of sliding local blocks into a large containing tensor.

Warning

Currently, only unbatched (3D) or batched (4D) image-like output tensors are supported.

See [`torch.nn.Fold`](torch.nn.Fold.html#torch.nn.Fold) for details

Return type:

[*Tensor*](../tensors.html#torch.Tensor)