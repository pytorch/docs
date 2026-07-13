# torch.linalg.polar

torch.linalg.polar(*A*, ***, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/9abc5460749ef85e489d960cb5facefc8cc1eb7c/torch/linalg/__init__.py#L2973)

Computes the polar decomposition of a matrix.

Letting K\mathbb{K}K be R\mathbb{R}R or C\mathbb{C}C,
the **polar decomposition** of a matrix
A∈Km×nA \in \mathbb{K}^{m \times n}A∈Km×n with m >= n is defined as

A=UHU∈Km×n,H∈Kn×nA = UH\mathrlap{\qquad U \in \mathbb{K}^{m \times n}, H \in \mathbb{K}^{n \times n}}A=UHU∈Km×n,H∈Kn×n

where UUU has orthonormal columns (it is orthogonal in the real case and
unitary in the complex case) and HHH is symmetric positive-semidefinite in
the real case and Hermitian positive-semidefinite in the complex case.

The orthogonal factor UUU is the closest matrix with orthonormal columns to
AAA in the Frobenius norm, which makes the polar decomposition a useful tool
for orthogonalization.

Note

`torch.linalg.polar()` computes the polar decomposition of a matrix, like
SciPy's [scipy.linalg.polar](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.polar.html).
It is not related to [`torch.polar()`](torch.polar.html#torch.polar), which constructs a complex tensor
from absolute values and angles like C++'s std::polar.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

On CUDA, this is computed with the QR-based Dynamically Weighted Halley (QDWH)
algorithm via cuSOLVER when [nvmath-python](https://pypi.org/project/nvmath-python/)
is installed and the cuSOLVER runtime is >= 12.2 (CUDA 13.2, which introduces
the required `cusolverDnXpolar` routine); otherwise (and on CPU) it falls back
to an SVD-based computation.

Note

This function is not differentiable. Calling it on a tensor that requires
grad and backpropagating raises an error; an autograd formula may be added
in a future release.

Warning

This function is "experimental" and it may change in a future PyTorch release.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) with m >= n, where * is zero or
more batch dimensions.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - output tuple of two tensors. Ignored if None. Default: None.

Returns:

A named tuple (U, H).

Examples:

```
>>> A = torch.randn(4, 3)
>>> U, H = torch.linalg.polar(A)
>>> torch.dist(U @ H, A)
tensor(7.1512e-07)
>>> torch.dist(U.mT @ U, torch.eye(3))
tensor(4.8995e-07)
```