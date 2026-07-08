# torch.nn.functional.lp_pool1d

torch.nn.functional.lp_pool1d(*input*, *norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/nn/functional.py#L1207)

Apply a 1D power-average pooling over an input signal composed of several input planes.

If the sum of all inputs to the power of p is
zero, the gradient is set to zero as well.

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the left
padding or the input. Sliding windows that would start in the right padded region are ignored.

See [`LPPool1d`](torch.nn.LPPool1d.html#torch.nn.LPPool1d) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)