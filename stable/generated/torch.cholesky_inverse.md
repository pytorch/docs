# torch.cholesky_inverse

torch.cholesky_inverse(*L*, *upper=False*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the inverse of a complex Hermitian or real symmetric
positive-definite matrix given its Cholesky decomposition.

Let AAA be a complex Hermitian or real symmetric positive-definite matrix,
and LLL its Cholesky decomposition such that:

A=LLHA = LL^{\text{H}}A=LLH

where LHL^{\text{H}}LH is the conjugate transpose when LLL is complex,
and the transpose when LLL is real-valued.

Computes the inverse matrix A−1A^{-1}A−1.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if AAA is a batch of matrices
then the output has the same batch dimensions.

Parameters:

- **L** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of lower or upper triangular Cholesky decompositions of
symmetric or Hermitian positive-definite matrices.
- **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - flag that indicates whether LLL is lower triangular
or upper triangular. Default: `False`

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Example:

```
>>> A = torch.randn(3, 3)
>>> A = A @ A.T + torch.eye(3) * 1e-3 # Creates a symmetric positive-definite matrix
>>> L = torch.linalg.cholesky(A) # Extract Cholesky decomposition
>>> torch.cholesky_inverse(L)
tensor([[ 1.9314, 1.2251, -0.0889],
 [ 1.2251, 2.4439, 0.2122],
 [-0.0889, 0.2122, 0.1412]])
>>> A.inverse()
tensor([[ 1.9314, 1.2251, -0.0889],
 [ 1.2251, 2.4439, 0.2122],
 [-0.0889, 0.2122, 0.1412]])

>>> A = torch.randn(3, 2, 2, dtype=torch.complex64)
>>> A = A @ A.mH + torch.eye(2) * 1e-3 # Batch of Hermitian positive-definite matrices
>>> L = torch.linalg.cholesky(A)
>>> torch.dist(torch.inverse(A), torch.cholesky_inverse(L))
tensor(5.6358e-7)
```