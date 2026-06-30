# torch.linalg.eigvals

torch.linalg.eigvals(*A*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/linalg/__init__.py#L584)

Computes the eigenvalues of a square matrix.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
the **eigenvalues** of a square matrix A∈Kn×nA \in \mathbb{K}^{n \times n}A∈Kn×n are defined
as the roots (counted with multiplicity) of the polynomial p of degree n given by

p(λ)=det⁡(A−λIn)λ∈Cp(\lambda) = \operatorname{det}(A - \lambda \mathrm{I}_n)\mathrlap{\qquad \lambda \in \mathbb{C}}p(λ)=det(A−λIn​)λ∈C

where In\mathrm{I}_nIn​ is the n-dimensional identity matrix.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

The returned eigenvalues are not guaranteed to be in any specific order.

Note

The eigenvalues of a real matrix may be complex, as the roots of a real polynomial may be complex.

The eigenvalues of a matrix are always well-defined, even when the matrix is not diagonalizable.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU.

See also

[`torch.linalg.eig()`](torch.linalg.eig.html#torch.linalg.eig) computes the full eigenvalue decomposition.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Returns:

A complex-valued tensor containing the eigenvalues even when `A` is real.

Examples:

```
>>> A = torch.randn(2, 2, dtype=torch.complex128)
>>> L = torch.linalg.eigvals(A)
>>> L
tensor([ 1.1226+0.5738j, -0.7537-0.1286j], dtype=torch.complex128)

>>> torch.dist(L, torch.linalg.eig(A).eigenvalues)
tensor(2.4576e-07)
```