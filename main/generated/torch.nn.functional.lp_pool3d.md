# torch.nn.functional.lp_pool3d

torch.nn.functional.lp_pool3d(*input*, *norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/nn/functional.py#L1111)

Apply a 3D power-average pooling over an input signal composed of several input planes.

If the sum of all inputs to the power of p is
zero, the gradient is set to zero as well.

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the left
padding or the input. Sliding windows that would start in the right padded region are ignored.

See [`LPPool3d`](torch.nn.LPPool3d.html#torch.nn.LPPool3d) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)