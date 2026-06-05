# torch.linalg.ldl_solve

torch.linalg.ldl_solve(*LD*, *pivots*, *B*, ***, *hermitian=False*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/linalg/__init__.py#L1032)

Computes the solution of a system of linear equations using the LDL factorization.

`LD` and `pivots` are the compact representation of the LDL factorization and
are expected to be computed by [`torch.linalg.ldl_factor_ex()`](torch.linalg.ldl_factor_ex.html#torch.linalg.ldl_factor_ex).
`hermitian` argument to this function should be the same
as the corresponding arguments in [`torch.linalg.ldl_factor_ex()`](torch.linalg.ldl_factor_ex.html#torch.linalg.ldl_factor_ex).

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

Warning

This function is "experimental" and it may change in a future PyTorch release.

Parameters:

- **LD** ([*Tensor*](../tensors.html#torch.Tensor)) - the n times n matrix or the batch of such matrices of size
(*, n, n) where * is one or more batch dimensions.
- **pivots** ([*Tensor*](../tensors.html#torch.Tensor)) - the pivots corresponding to the LDL factorization of `LD`.
- **B** ([*Tensor*](../tensors.html#torch.Tensor)) - right-hand side tensor of shape (*, n, k).

Keyword Arguments:

- **hermitian** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to consider the decomposed matrix to be Hermitian or symmetric.
For real-valued matrices, this switch has no effect. Default: False.
- **out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - output tensor. B may be passed as out and the result is computed in-place on B.
Ignored if None. Default: None.

Examples:

```
>>> A = torch.randn(2, 3, 3)
>>> A = A @ A.mT # make symmetric
>>> LD, pivots, info = torch.linalg.ldl_factor_ex(A)
>>> B = torch.randn(2, 3, 4)
>>> X = torch.linalg.ldl_solve(LD, pivots, B)
>>> torch.linalg.norm(A @ X - B)
>>> tensor(0.0001)
```