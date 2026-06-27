# torch.nn.functional.fold

torch.nn.functional.fold(*input*, *output_size*, *kernel_size*, *dilation=1*, *padding=0*, *stride=1*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/nn/functional.py#L6176)

Combine an array of sliding local blocks into a large containing tensor.

Warning

Currently, only unbatched (3D) or batched (4D) image-like output tensors are supported.

See [`torch.nn.Fold`](torch.nn.Fold.html#torch.nn.Fold) for details

Return type:

[*Tensor*](../tensors.html#torch.Tensor)