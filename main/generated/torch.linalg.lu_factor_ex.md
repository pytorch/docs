# torch.linalg.lu_factor_ex

torch.linalg.lu_factor_ex(*A*, ***, *pivot=True*, *check_errors=False*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/linalg/__init__.py#L2531)

This is a version of [`lu_factor()`](torch.linalg.lu_factor.html#torch.linalg.lu_factor) that does not perform error checks unless `check_errors`= True.
It also returns the `info` tensor returned by [LAPACK's getrf](https://www.netlib.org/lapack/explore-html/).

Note

When the inputs are on a CUDA device, this function synchronizes only when `check_errors`= True.

Warning

This function is "experimental" and it may change in a future PyTorch release.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, n) where * is zero or more batch dimensions.

Keyword Arguments:

- **pivot** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Whether to compute the LU decomposition with partial pivoting, or the regular LU
decomposition. `pivot`= False not supported on CPU. Default: True.
- **check_errors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - controls whether to check the content of `infos` and raise
an error if it is non-zero. Default: False.
- **out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - tuple of three tensors to write the output to. Ignored if None. Default: None.

Returns:

A named tuple (LU, pivots, info).