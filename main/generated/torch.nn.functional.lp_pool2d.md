# torch.nn.functional.lp_pool2d

torch.nn.functional.lp_pool2d(*input*, *norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/nn/functional.py#L1160)

Apply a 2D power-average pooling over an input signal composed of several input planes.

If the sum of all inputs to the power of p is
zero, the gradient is set to zero as well.

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the left
padding or the input. Sliding windows that would start in the right padded region are ignored.

See [`LPPool2d`](torch.nn.LPPool2d.html#torch.nn.LPPool2d) for details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)