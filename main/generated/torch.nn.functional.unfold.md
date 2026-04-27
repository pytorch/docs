# torch.nn.functional.unfold

torch.nn.functional.unfold(*input*, *kernel_size*, *dilation=1*, *padding=0*, *stride=1*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/nn/functional.py#L5757)

Extract sliding local blocks from a batched input tensor.

Warning

Currently, only 4-D input tensors (batched image-like tensors) are
supported.

Warning

More than one element of the unfolded tensor may refer to a single
memory location. As a result, in-place operations (especially ones that
are vectorized) may result in incorrect behavior. If you need to write
to the tensor, please clone it first.

See [`torch.nn.Unfold`](torch.nn.Unfold.html#torch.nn.Unfold) for details

Return type:

[*Tensor*](../tensors.html#torch.Tensor)