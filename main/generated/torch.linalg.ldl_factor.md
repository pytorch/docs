# torch.linalg.ldl_factor

torch.linalg.ldl_factor(*A*, ***, *hermitian=False*, *out=None*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/linalg/__init__.py#L914)

Computes a compact representation of the LDL factorization of a Hermitian or symmetric (possibly indefinite) matrix.

When `A` is complex valued it can be Hermitian (`hermitian`= True)
or symmetric (`hermitian`= False).

The factorization is of the form A=LDLTA = L D L^TA=LDLT.
If `hermitian` is True then transpose operation is the conjugate transpose.

LLL (or UUU) and DDD are stored in compact form in `LD`.
They follow the format specified by [LAPACK's sytrf](https://www.netlib.org/lapack/explore-html/) function.
These tensors may be used in [`torch.linalg.ldl_solve()`](torch.linalg.ldl_solve.html#torch.linalg.ldl_solve) to solve linear systems.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

Note

When inputs are on a CUDA device, this function synchronizes that device with the CPU. For a version of this function that does not synchronize, see [`torch.linalg.ldl_factor_ex()`](torch.linalg.ldl_factor_ex.html#torch.linalg.ldl_factor_ex).

Parameters:

**A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n, n) where * is zero or more batch dimensions
consisting of symmetric or Hermitian matrices.

Keyword Arguments:

- **hermitian** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether to consider the input to be Hermitian or symmetric.
For real-valued matrices, this switch has no effect. Default: False.
- **out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - tuple of two tensors to write the output to. Ignored if None. Default: None.

Returns:

A named tuple (LD, pivots).

Examples:

```
>>> A = torch.randn(3, 3)
>>> A = A @ A.mT # make symmetric
>>> A
tensor([[7.2079, 4.2414, 1.9428],
 [4.2414, 3.4554, 0.3264],
 [1.9428, 0.3264, 1.3823]])
>>> LD, pivots = torch.linalg.ldl_factor(A)
>>> LD
tensor([[ 7.2079, 0.0000, 0.0000],
 [ 0.5884, 0.9595, 0.0000],
 [ 0.2695, -0.8513, 0.1633]])
>>> pivots
tensor([1, 2, 3], dtype=torch.int32)
```