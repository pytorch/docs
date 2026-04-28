# torch.log1p

torch.log1p(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the natural logarithm of (1 + `input`).

yi=log⁡e(xi+1)y_i = \log_{e} (x_i + 1)

yi​=loge​(xi​+1)

Note

This function is more accurate than [`torch.log()`](torch.log.html#torch.log) for small
values of `input`

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(5)
>>> a
tensor([-1.0090, -0.9923, 1.0249, -0.5372, 0.2492])
>>> torch.log1p(a)
tensor([ nan, -4.8653, 0.7055, -0.7705, 0.2225])
```