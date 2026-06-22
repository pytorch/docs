# torch.linalg.eigvalsh

torch.linalg.eigvalsh(*A*, *UPLO='L'*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/linalg/__init__.py#L765)

Computes the eigenvalues of a complex Hermitian or real symmetric matrix.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
the **eigenvalues** of a complex Hermitian or real symmetric matrix A∈Kn×nA \in \mathbb{K}^{n \times n}A∈Kn×n
are defined as the roots (counted with multiplicity) of the polynomial p of degree n given by

p(λ)=det⁡(A−λIn)λ∈Rp(\lambda) = \operatorname{det}(A - \lambda \mathrm{I}_n)\mathrlap{\qquad \lambda \in \mathbb{R}}p(λ)=det(A−λIn​)λ∈R

where In\mathrm{I}_nIn​ is the n-dimensional identity matrix.
The eigenvalues of a real symmetric or complex Hermitian matrix are always real.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

The eigenvalues are returned in ascending order.

`A` is assumed to be Hermitian (resp. symmetric), but this is not checked internally, instead:

- If `UPLO`= 'L' (default), only the lower triangular part of the matrix is used in the computation.
- If `UPLO`= 'U', only the upper triangular part of the matrix is used.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU.

See also

[`torch.linalg.eigh()`](torch.linalg.eigh.html#torch.linalg.eigh) computes the full eigenvalue decomposition.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of symmetric or Hermitian matrices.
- **UPLO** (*'L'**,**'U'**,**optional*) - controls whether to use the upper or lower triangular part
of `A` in the computations. Default: 'L'.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Returns:

A real-valued tensor containing the eigenvalues even when `A` is complex.
The eigenvalues are returned in ascending order.

Examples:

```
>>> A = torch.randn(2, 2, dtype=torch.complex128)
>>> A = A + A.T.conj() # creates a Hermitian matrix
>>> A
tensor([[2.9228+0.0000j, 0.2029-0.0862j],
 [0.2029+0.0862j, 0.3464+0.0000j]], dtype=torch.complex128)
>>> torch.linalg.eigvalsh(A)
tensor([0.3277, 2.9415], dtype=torch.float64)

>>> A = torch.randn(3, 2, 2, dtype=torch.float64)
>>> A = A + A.mT # creates a batch of symmetric matrices
>>> torch.linalg.eigvalsh(A)
tensor([[ 2.5797, 3.4629],
 [-4.1605, 1.3780],
 [-3.1113, 2.7381]], dtype=torch.float64)
```