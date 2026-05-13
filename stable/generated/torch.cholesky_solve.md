# torch.cholesky_solve

torch.cholesky_solve(*B*, *L*, *upper=False*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the solution of a system of linear equations with complex Hermitian
or real symmetric positive-definite lhs given its Cholesky decomposition.

Let AAA be a complex Hermitian or real symmetric positive-definite matrix,
and LLL its Cholesky decomposition such that:

A=LLHA = LL^{\text{H}}A=LLH

where LHL^{\text{H}}LH is the conjugate transpose when LLL is complex,
and the transpose when LLL is real-valued.

Returns the solution XXX of the following linear system:

AX=BAX = BAX=B

Supports inputs of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if AAA or BBB is a batch of matrices
then the output has the same batch dimensions.

Parameters:

- **B** ([*Tensor*](../tensors.html#torch.Tensor)) - right-hand side tensor of shape (*, n, k)
where ∗*∗ is zero or more batch dimensions
- **L** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of lower or upper triangular Cholesky decompositions of
symmetric or Hermitian positive-definite matrices.
- **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - flag that indicates whether LLL is lower triangular
or upper triangular. Default: `False`.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Example:

```
>>> A = torch.randn(3, 3)
>>> A = A @ A.T + torch.eye(3) * 1e-3 # Creates a symmetric positive-definite matrix
>>> L = torch.linalg.cholesky(A) # Extract Cholesky decomposition
>>> B = torch.randn(3, 2)
>>> torch.cholesky_solve(B, L)
tensor([[ -8.1625, 19.6097],
 [ -5.8398, 14.2387],
 [ -4.3771, 10.4173]])
>>> A.inverse() @ B
tensor([[ -8.1626, 19.6097],
 [ -5.8398, 14.2387],
 [ -4.3771, 10.4173]])

>>> A = torch.randn(3, 2, 2, dtype=torch.complex64)
>>> A = A @ A.mH + torch.eye(2) * 1e-3 # Batch of Hermitian positive-definite matrices
>>> L = torch.linalg.cholesky(A)
>>> B = torch.randn(2, 1, dtype=torch.complex64)
>>> X = torch.cholesky_solve(B, L)
>>> torch.dist(X, A.inverse() @ B)
tensor(1.6881e-5)
```