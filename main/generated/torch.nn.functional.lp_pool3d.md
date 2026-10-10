# torch.nn.functional.lp_pool3d

torch.nn.functional.lp_pool3d(*input*, *norm_type*, *kernel_size*, *stride=None*, *ceil_mode=False*)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/nn/functional.py#L1111)

Apply a 3D power-average pooling over an input signal composed of several input planes.

If the sum of all inputs to the power of p is
zero, the gradient is set to zero as well.

When `ceil_mode` is `True`, sliding windows may go off-bounds if they start within the left
padding or the input. Sliding windows that would start in the right padded region are ignored.

See [`LPPool3d`](torch.nn.LPPool3d.html#torch.nn.LPPool3d) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **norm_type** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*float*](https://docs.python.org/3/builtins/functions.html#float)) - the power ppp used to compute pooling.
Must be non-zero; positive and negative infinity are supported.
- **kernel_size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - the size of the pooling window.
- **stride** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or*[*tuple*](https://docs.python.org/3/builtins/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,**optional*) - the stride between windows.
Default: `kernel_size`.
- **ceil_mode** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,**optional*) - when `True`, use `ceil` instead of
`floor` to compute the output shape. Default: `False`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)