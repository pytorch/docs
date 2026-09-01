# torch.linalg.slogdet

torch.linalg.slogdet(*A*, ***, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/linalg/__init__.py#L424)

Computes the sign and natural logarithm of the absolute value of the determinant of a square matrix.

For complex `A`, it returns the sign and the natural logarithm of the modulus of the
determinant, that is, a logarithmic polar decomposition of the determinant.

The determinant can be recovered as sign * exp(logabsdet).
When a matrix has a determinant of zero, it returns (0, -inf).

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

See also

[`torch.linalg.det()`](torch.linalg.det.html#torch.linalg.det) computes the determinant of square matrices.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - output tuple of two tensors. Ignored if None. Default: None.

Returns:

A named tuple (sign, logabsdet).

sign will have the same dtype as `A`.

logabsdet will always be real-valued, even when `A` is complex.

Examples:

```
>>> A = torch.randn(3, 3)
>>> A
tensor([[ 0.0032, -0.2239, -1.1219],
 [-0.6690, 0.1161, 0.4053],
 [-1.6218, -0.9273, -0.0082]])
>>> torch.linalg.det(A)
tensor(-0.7576)
>>> torch.logdet(A)
tensor(nan)
>>> torch.linalg.slogdet(A)
torch.return_types.linalg_slogdet(sign=tensor(-1.), logabsdet=tensor(-0.2776))
```