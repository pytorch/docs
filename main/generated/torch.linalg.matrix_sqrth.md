# torch.linalg.matrix_sqrth

torch.linalg.matrix_sqrth(*A*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/linalg/__init__.py#L2213)

Computes the principal square root of a symmetric (resp. Hermitian) positive-definite matrix.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
for a symmetric (resp. Hermitian) positive-definite matrix A∈Kn×nA \in \mathbb{K}^{n \times n}A∈Kn×n,
this function returns the unique symmetric (resp. Hermitian) positive-definite matrix
X∈Kn×nX \in \mathbb{K}^{n \times n}X∈Kn×n such that

XX=A.XX = A.

XX=A.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

Note

Only the lower triangular part of `A` is used in the computation, and
`A` is assumed to be symmetric (resp. Hermitian). See [`torch.linalg.eigh()`](torch.linalg.eigh.html#torch.linalg.eigh).

See also

[`torch.linalg.cholesky()`](torch.linalg.cholesky.html#torch.linalg.cholesky) computes a different factorization of a symmetric
(resp. Hermitian) positive-definite matrix.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of symmetric (resp. Hermitian) positive-definite matrices.

Examples:

```
>>> A = torch.tensor([[2., 0.], [0., 9.]])
>>> torch.linalg.matrix_sqrth(A)
tensor([[1.4142, 0.0000],
 [0.0000, 3.0000]])

>>> A = torch.randn(2, 3, 3)
>>> A = A @ A.mT + 3 * torch.eye(3) # batch of symmetric positive-definite matrices
>>> X = torch.linalg.matrix_sqrth(A)
>>> torch.allclose(X @ X, A, atol=1e-5)
True
```