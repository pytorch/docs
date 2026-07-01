# torch.linalg.det

torch.linalg.det(*A*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/df6ed392bccc6625dbf4f6a82bcecee03433aa18/torch/linalg/__init__.py#L390)

Computes the determinant of a square matrix.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

See also

[`torch.linalg.slogdet()`](torch.linalg.slogdet.html#torch.linalg.slogdet) computes the sign and natural logarithm of the absolute
value of the determinant of square matrices.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Examples:

```
>>> A = torch.randn(3, 3)
>>> torch.linalg.det(A)
tensor(0.0934)

>>> A = torch.randn(3, 2, 2)
>>> torch.linalg.det(A)
tensor([1.1990, 0.4099, 0.7386])
```