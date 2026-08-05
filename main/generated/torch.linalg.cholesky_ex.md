# torch.linalg.cholesky_ex

torch.linalg.cholesky_ex(*A*, ***, *upper=False*, *check_errors=False*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/linalg/__init__.py#L148)

Computes the Cholesky decomposition of a complex Hermitian or real
symmetric positive-definite matrix.

This function skips the (slow) error checking and error message construction
of [`torch.linalg.cholesky()`](torch.linalg.cholesky.html#torch.linalg.cholesky), instead directly returning the LAPACK
error codes as part of a named tuple `(L, info)`. This makes this function
a faster way to check if a matrix is positive-definite, and it provides an
opportunity to handle decomposition errors more gracefully or performantly
than [`torch.linalg.cholesky()`](torch.linalg.cholesky.html#torch.linalg.cholesky) does.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

If `A` is not a Hermitian positive-definite matrix, or if it's a batch of matrices
and one or more of them is not a Hermitian positive-definite matrix,
then `info` stores a positive integer for the corresponding matrix.
The positive integer indicates the order of the leading minor that is not positive-definite,
and the decomposition could not be completed.
`info` filled with zeros indicates that the decomposition was successful.
If `check_errors=True` and `info` contains positive integers, then a RuntimeError is thrown.

Note

When the inputs are on a CUDA device, this function synchronizes only when `check_errors`= True.

Warning

This function is "experimental" and it may change in a future PyTorch release.

See also

[`torch.linalg.cholesky()`](torch.linalg.cholesky.html#torch.linalg.cholesky) is a NumPy compatible variant that always checks for errors.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - the Hermitian n times n matrix or the batch of such matrices of size
(*, n, n) where * is one or more batch dimensions.

Keyword Arguments:

- **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to return an upper triangular matrix.
The tensor returned with upper=True is the conjugate transpose of the tensor
returned with upper=False.
- **check_errors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - controls whether to check the content of `infos`. Default: False.
- **out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - tuple of two tensors to write the output to. Ignored if None. Default: None.

Examples:

```
>>> A = torch.randn(2, 2, dtype=torch.complex128)
>>> A = A @ A.t().conj() # creates a Hermitian positive-definite matrix
>>> L, info = torch.linalg.cholesky_ex(A)
>>> A
tensor([[ 2.3792+0.0000j, -0.9023+0.9831j],
 [-0.9023-0.9831j, 0.8757+0.0000j]], dtype=torch.complex128)
>>> L
tensor([[ 1.5425+0.0000j, 0.0000+0.0000j],
 [-0.5850-0.6374j, 0.3567+0.0000j]], dtype=torch.complex128)
>>> info
tensor(0, dtype=torch.int32)
```