# torch.linalg.svdvals

torch.linalg.svdvals(*A*, ***, *driver=None*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/a7ff5691322735e9c4fc9f23bc19be9040aa9d50/torch/linalg/__init__.py#L1888)

Computes the singular values of a matrix.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

The singular values are returned in descending order.

Note

This function is equivalent to NumPy's linalg.svd(A, compute_uv=False).

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU.

See also

[`torch.linalg.svd()`](torch.linalg.svd.html#torch.linalg.svd) computes the full singular value decomposition.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) where * is zero or more batch dimensions.

Keyword Arguments:

- **driver** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name of the cuSOLVER method to be used. This keyword argument only works on CUDA inputs.
Available options are: None, gesvd, gesvdj, and gesvda.
Check [`torch.linalg.svd()`](torch.linalg.svd.html#torch.linalg.svd) for details.
Default: None.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Returns:

A real-valued tensor, even when `A` is complex.

Examples:

```
>>> A = torch.randn(5, 3)
>>> S = torch.linalg.svdvals(A)
>>> S
tensor([2.5139, 2.1087, 1.1066])

>>> torch.dist(S, torch.linalg.svd(A, full_matrices=False).S)
tensor(2.4576e-07)
```