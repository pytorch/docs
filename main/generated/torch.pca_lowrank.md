# torch.pca_lowrank

torch.pca_lowrank(*A*, *q=None*, *center=True*, *niter=2*)[[source]](https://github.com/pytorch/pytorch/blob/051c786d044a8aa490884192d549c8057aa4d2e7/torch/_lowrank.py#L183)

Performs linear Principal Component Analysis (PCA) on a low-rank
matrix, batches of such matrices, or sparse matrix.

This function returns a namedtuple `(U, S, V)` which is the
nearly optimal approximation of a singular value decomposition of
a centered matrix AAA such that A≈Udiag⁡(S)VHA \approx U \operatorname{diag}(S) V^{\text{H}}A≈Udiag(S)VH

Note

The relation of `(U, S, V)` to PCA is as follows:

- AAA is a data matrix with `m` samples and
`n` features
- the VVV columns represent the principal directions
- S∗∗2/(m−1)S ** 2 / (m - 1)S∗∗2/(m−1) contains the eigenvalues of
ATA/(m−1)A^T A / (m - 1)ATA/(m−1) which is the covariance of
`A` when `center=True` is provided.
- `matmul(A, V[:, :k])` projects data to the first k
principal components

Note

Different from the standard SVD, the size of returned
matrices depend on the specified rank and q
values as follows:

> - UUU is m x q matrix
> - SSS is q-vector
> - VVV is n x q matrix

Note

To obtain repeatable results, reset the seed for the
pseudorandom number generator

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor of size (∗,m,n)(*, m, n)(∗,m,n)
- **q** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - a slightly overestimated rank of
AAA. By default, `q = min(6, m,
n)`.
- **center** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - if True, center the input tensor,
otherwise, assume that the input is
centered.
- **niter** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the number of subspace iterations to
conduct; niter must be a nonnegative
integer, and defaults to 2.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor)]

References:

```
- Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
 structure with randomness: probabilistic algorithms for
 constructing approximate matrix decompositions,
 arXiv:0909.4061 [math.NA; math.PR], 2009 (available at
 `arXiv <http://arxiv.org/abs/0909.4061>`_).
```