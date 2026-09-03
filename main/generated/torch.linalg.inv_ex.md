# torch.linalg.inv_ex

torch.linalg.inv_ex(*A*, ***, *check_errors=False*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/linalg/__init__.py#L336)

Computes the inverse of a square matrix if it is invertible.

Returns a namedtuple `(inverse, info)`. `inverse` contains the result of
inverting `A` and `info` stores the LAPACK error codes.

If `A` is not an invertible matrix, or if it's a batch of matrices
and one or more of them is not an invertible matrix,
then `info` stores a positive integer for the corresponding matrix.
The positive integer indicates the diagonal element of the LU decomposition of
the input matrix that is exactly zero.
`info` filled with zeros indicates that the inversion was successful.
If `check_errors=True` and `info` contains positive integers, then a RuntimeError is thrown.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

Note

When the inputs are on a CUDA device, this function synchronizes only when `check_errors`= True.

Warning

This function is "experimental" and it may change in a future PyTorch release.

See also

[`torch.linalg.inv()`](torch.linalg.inv.html#torch.linalg.inv) is a NumPy compatible variant that always checks for errors.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of square matrices.
- **check_errors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - controls whether to check the content of `info`. Default: False.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - tuple of two tensors to write the output to. Ignored if None. Default: None.

Examples:

```
>>> A = torch.randn(3, 3)
>>> Ainv, info = torch.linalg.inv_ex(A)
>>> torch.dist(torch.linalg.inv(A), Ainv)
tensor(0.)
>>> info
tensor(0, dtype=torch.int32)
```