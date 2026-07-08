# torch.linalg.solve_ex

torch.linalg.solve_ex(*A*, *B*, ***, *left=True*, *check_errors=False*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/linalg/__init__.py#L294)

A version of [`solve()`](torch.linalg.solve.html#torch.linalg.solve) that does not perform error checks unless `check_errors`= True.
It also returns the `info` tensor returned by [LAPACK's getrf](https://www.netlib.org/lapack/explore-html/).

Note

When the inputs are on a CUDA device, this function synchronizes only when `check_errors`= True.

Warning

This function is "experimental" and it may change in a future PyTorch release.

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions.

Keyword Arguments:

- **left** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to solve the system AX=BAX=BAX=B or XA=BXA = BXA=B. Default: True.
- **check_errors** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - controls whether to check the content of `infos` and raise
an error if it is non-zero. Default: False.
- **out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - tuple of two tensors to write the output to. Ignored if None. Default: None.

Returns:

A named tuple (result, info).

Examples:

```
>>> A = torch.randn(3, 3)
>>> Ainv, info = torch.linalg.solve_ex(A)
>>> torch.dist(torch.linalg.inv(A), Ainv)
tensor(0.)
>>> info
tensor(0, dtype=torch.int32)
```