# torch.triangular_solve

torch.triangular_solve(*b*, *A*, *upper=True*, *transpose=False*, *unitriangular=False*, ***, *out=None*)

Solves a system of equations with a square upper or lower triangular invertible matrix AAA
and multiple right-hand sides bbb.

In symbols, it solves AX=bAX = bAX=b and assumes AAA is square upper-triangular
(or lower-triangular if `upper`= False) and does not have zeros on the diagonal.

torch.triangular_solve(b, A) can take in 2D inputs b, A or inputs that are
batches of 2D matrices. If the inputs are batches, then returns
batched outputs X

If the diagonal of `A` contains zeros or elements that are very close to zero and
`unitriangular`= False (default) or if the input matrix is badly conditioned,
the result may contain NaN s.

Supports input of float, double, cfloat and cdouble data types.

Warning

`torch.triangular_solve()` is deprecated in favor of [`torch.linalg.solve_triangular()`](torch.linalg.solve_triangular.html#torch.linalg.solve_triangular)
and will be removed in a future PyTorch release.
[`torch.linalg.solve_triangular()`](torch.linalg.solve_triangular.html#torch.linalg.solve_triangular) has its arguments reversed and does not return a
copy of one of the inputs.

`X = torch.triangular_solve(B, A).solution` should be replaced with

```
X = torch.linalg.solve_triangular(A, B)
```

Parameters:

- **b** ([*Tensor*](../tensors.html#torch.Tensor)) - multiple right-hand sides of size (∗,m,k)(*, m, k)(∗,m,k) where
∗*∗ is zero of more batch dimensions
- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - the input triangular coefficient matrix of size (∗,m,m)(*, m, m)(∗,m,m)
where ∗*∗ is zero or more batch dimensions
- **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether AAA is upper or lower triangular. Default: `True`.
- **transpose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - solves op(A)X = b where op(A) = A^T if this flag is `True`,
and op(A) = A if it is `False`. Default: `False`.
- **unitriangular** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether AAA is unit triangular.
If True, the diagonal elements of AAA are assumed to be
1 and not referenced from AAA. Default: `False`.

Keyword Arguments:

**out** (*(*[*Tensor*](../tensors.html#torch.Tensor)*,*[*Tensor*](../tensors.html#torch.Tensor)*)**,**optional*) - tuple of two tensors to write
the output to. Ignored if None. Default: None.

Returns:

A namedtuple (solution, cloned_coefficient) where cloned_coefficient
is a clone of AAA and solution is the solution XXX to AX=bAX = bAX=b
(or whatever variant of the system of equations, depending on the keyword arguments.)

Examples:

```
>>> A = torch.randn(2, 2).triu()
>>> A
tensor([[ 1.1527, -1.0753],
 [ 0.0000, 0.7986]])
>>> b = torch.randn(2, 3)
>>> b
tensor([[-0.0210, 2.3513, -1.5492],
 [ 1.5429, 0.7403, -1.0243]])
>>> torch.triangular_solve(b, A)
torch.return_types.triangular_solve(
solution=tensor([[ 1.7841, 2.9046, -2.5405],
 [ 1.9320, 0.9270, -1.2826]]),
cloned_coefficient=tensor([[ 1.1527, -1.0753],
 [ 0.0000, 0.7986]]))
```