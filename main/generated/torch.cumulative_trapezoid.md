# torch.cumulative_trapezoid

torch.cumulative_trapezoid(*y*, *x=None*, ***, *dx=None*, *dim=-1*) → [Tensor](../tensors.html#torch.Tensor)

Cumulatively computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)
along `dim`. By default the spacing between elements is assumed to be 1, but
`dx` can be used to specify a different constant spacing, and `x` can be
used to specify arbitrary spacing along `dim`.

For more details, please read [`torch.trapezoid()`](torch.trapezoid.html#torch.trapezoid). The difference between [`torch.trapezoid()`](torch.trapezoid.html#torch.trapezoid)
and this function is that, [`torch.trapezoid()`](torch.trapezoid.html#torch.trapezoid) returns a value for each integration,
where as this function returns a cumulative value for every spacing within the integration. This
is analogous to how .sum returns a value and .cumsum returns a cumulative sum.

Parameters:

- **y** ([*Tensor*](../tensors.html#torch.Tensor)) - Values to use when computing the trapezoidal rule.
- **x** ([*Tensor*](../tensors.html#torch.Tensor)) - If specified, defines spacing between values as specified above.

Keyword Arguments:

- **dx** ([*float*](https://docs.python.org/3/library/functions.html#float)) - constant spacing between values. If neither `x` or `dx`
are specified then this defaults to 1. Effectively multiplies the result by its value.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The dimension along which to compute the trapezoidal rule.
The last (inner-most) dimension by default.

Examples:

```
>>> # Cumulatively computes the trapezoidal rule in 1D, spacing is implicitly 1.
>>> y = torch.tensor([1, 5, 10])
>>> torch.cumulative_trapezoid(y)
tensor([3., 10.5])

>>> # Computes the same trapezoidal rule directly up to each element to verify
>>> (1 + 5) / 2
3.0
>>> (1 + 10 + 10) / 2
10.5

>>> # Cumulatively computes the trapezoidal rule in 1D with constant spacing of 2
>>> # NOTE: the result is the same as before, but multiplied by 2
>>> torch.cumulative_trapezoid(y, dx=2)
tensor([6., 21.])

>>> # Cumulatively computes the trapezoidal rule in 1D with arbitrary spacing
>>> x = torch.tensor([1, 3, 6])
>>> torch.cumulative_trapezoid(y, x)
tensor([6., 28.5])

>>> # Computes the same trapezoidal rule directly up to each element to verify
>>> ((3 - 1) * (1 + 5)) / 2
6.0
>>> ((3 - 1) * (1 + 5) + (6 - 3) * (5 + 10)) / 2
28.5

>>> # Cumulatively computes the trapezoidal rule for each row of a 3x3 matrix
>>> y = torch.arange(9).reshape(3, 3)
tensor([[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]])
>>> torch.cumulative_trapezoid(y)
tensor([[ 0.5, 2.],
 [ 3.5, 8.],
 [ 6.5, 14.]])

>>> # Cumulatively computes the trapezoidal rule for each column of the matrix
>>> torch.cumulative_trapezoid(y, dim=0)
tensor([[ 1.5, 2.5, 3.5],
 [ 6.0, 8.0, 10.0]])

>>> # Cumulatively computes the trapezoidal rule for each row of a 3x3 ones matrix
>>> # with the same arbitrary spacing
>>> y = torch.ones(3, 3)
>>> x = torch.tensor([1, 3, 6])
>>> torch.cumulative_trapezoid(y, x)
tensor([[2., 5.],
 [2., 5.],
 [2., 5.]])

>>> # Cumulatively computes the trapezoidal rule for each row of a 3x3 ones matrix
>>> # with different arbitrary spacing per row
>>> y = torch.ones(3, 3)
>>> x = torch.tensor([[1, 2, 3], [1, 3, 5], [1, 4, 7]])
>>> torch.cumulative_trapezoid(y, x)
tensor([[1., 2.],
 [2., 4.],
 [3., 6.]])
```