# torch.svd_lowrank

torch.svd_lowrank(*A*, *q=6*, *niter=2*, *M=None*)[[source]](https://github.com/pytorch/pytorch/blob/7e9fd4e82a01d43fc8afdf03258cf85ee22db2ea/torch/_lowrank.py#L85)

Return the singular value decomposition `(U, S, V)` of a matrix,
batches of matrices, or a sparse matrix AAA such that
A≈Udiag⁡(S)VHA \approx U \operatorname{diag}(S) V^{\text{H}}A≈Udiag(S)VH. In case MMM is given, then
SVD is computed for the matrix A−MA - MA−M.

Note

The implementation is based on the Algorithm 5.1 from
Halko et al., 2009.

Note

For an adequate approximation of a k-rank matrix
AAA, where k is not known in advance but could be
estimated, the number of QQQ columns, q, can be
chosen according to the following criteria: in general,
k<=q<=min(2∗k,m,n)k <= q <= min(2*k, m, n)k<=q<=min(2∗k,m,n). For large low-rank
matrices, take q=k+5..10q = k + 5..10q=k+5..10. If k is
relatively small compared to min(m,n)min(m, n)min(m,n), choosing
q=k+0..2q = k + 0..2q=k+0..2 may be sufficient.

Note

This is a randomized method. To obtain repeatable results,
set the seed for the pseudorandom number generator

Note

In general, use the full-rank SVD implementation
[`torch.linalg.svd()`](torch.linalg.svd.html#torch.linalg.svd) for dense matrices due to its 10x
higher performance characteristics. The low-rank SVD
will be useful for huge sparse matrices that
[`torch.linalg.svd()`](torch.linalg.svd.html#torch.linalg.svd) cannot handle.

Args::

A (Tensor): the input tensor of size (∗,m,n)(*, m, n)(∗,m,n)

q (int, optional): a slightly overestimated rank of A.

niter (int, optional): the number of subspace iterations to

conduct; niter must be a nonnegative
integer, and defaults to 2

M (Tensor, optional): the input tensor's mean of size

(∗,m,n)(*, m, n)(∗,m,n), which will be broadcasted
to the size of A in this function.

References::

- Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
structure with randomness: probabilistic algorithms for
constructing approximate matrix decompositions,
arXiv:0909.4061 [math.NA; math.PR], 2009 (available at
[arXiv](https://arxiv.org/abs/0909.4061)).

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor), [*Tensor*](../tensors.html#torch.Tensor)]