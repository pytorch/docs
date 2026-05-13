# torch.cholesky

torch.cholesky(*input*, *upper=False*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the Cholesky decomposition of a symmetric positive-definite
matrix AAA or for batches of symmetric positive-definite matrices.

If `upper` is `True`, the returned matrix `U` is upper-triangular, and
the decomposition has the form:

A=UTUA = U^TUA=UTU

If `upper` is `False`, the returned matrix `L` is lower-triangular, and
the decomposition has the form:

A=LLTA = LL^TA=LLT

If `upper` is `True`, and AAA is a batch of symmetric positive-definite
matrices, then the returned tensor will be composed of upper-triangular Cholesky factors
of each of the individual matrices. Similarly, when `upper` is `False`, the returned
tensor will be composed of lower-triangular Cholesky factors of each of the individual
matrices.

Warning

`torch.cholesky()` is deprecated in favor of [`torch.linalg.cholesky()`](torch.linalg.cholesky.html#torch.linalg.cholesky)
and will be removed in a future PyTorch release.

`L = torch.cholesky(A)` should be replaced with

```
L = torch.linalg.cholesky(A)
```

`U = torch.cholesky(A, upper=True)` should be replaced with

```
U = torch.linalg.cholesky(A).mH
```

This transform will produce equivalent results for all valid (symmetric positive definite) inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor AAA of size (∗,n,n)(*, n, n)(∗,n,n) where * is zero or more
batch dimensions consisting of symmetric positive-definite matrices.
- **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - flag that indicates whether to return a
upper or lower triangular matrix. Default: `False`

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output matrix

Example:

```
>>> a = torch.randn(3, 3)
>>> a = a @ a.mT + 1e-3 # make symmetric positive-definite
>>> l = torch.cholesky(a)
>>> a
tensor([[ 2.4112, -0.7486, 1.4551],
 [-0.7486, 1.3544, 0.1294],
 [ 1.4551, 0.1294, 1.6724]])
>>> l
tensor([[ 1.5528, 0.0000, 0.0000],
 [-0.4821, 1.0592, 0.0000],
 [ 0.9371, 0.5487, 0.7023]])
>>> l @ l.mT
tensor([[ 2.4112, -0.7486, 1.4551],
 [-0.7486, 1.3544, 0.1294],
 [ 1.4551, 0.1294, 1.6724]])
>>> a = torch.randn(3, 2, 2) # Example for batched input
>>> a = a @ a.mT + 1e-03 # make symmetric positive-definite
>>> l = torch.cholesky(a)
>>> z = l @ l.mT
>>> torch.dist(z, a)
tensor(2.3842e-07)
```