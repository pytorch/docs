# torch.trapezoid

torch.trapezoid(*y*, *x=None*, ***, *dx=None*, *dim=-1*) → [Tensor](../tensors.html#torch.Tensor)

Computes the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule) along
`dim`. By default the spacing between elements is assumed to be 1, but
`dx` can be used to specify a different constant spacing, and `x` can be
used to specify arbitrary spacing along `dim`. Only one of `x` or `dx` should be specified.

Assuming `y` is a one-dimensional tensor with elements y0,y1,...,yn{y_0, y_1, ..., y_n}y0​,y1​,...,yn​,
the default computation is

∑i=1n12(yi+yi−1)\begin{aligned}
 \sum_{i = 1}^{n} \frac{1}{2} (y_i + y_{i-1})
\end{aligned}

i=1∑n​21​(yi​+yi−1​)​

When `dx` is specified the computation becomes

∑i=1nΔx2(yi+yi−1)\begin{aligned}
 \sum_{i = 1}^{n} \frac{\Delta x}{2} (y_i + y_{i-1})
\end{aligned}

i=1∑n​2Δx​(yi​+yi−1​)​

effectively multiplying the result by `dx`. When `x` is specified,
assuming `x` is also a one-dimensional tensor with
elements x0,x1,...,xn{x_0, x_1, ..., x_n}x0​,x1​,...,xn​, the computation becomes

∑i=1n(xi−xi−1)2(yi+yi−1)\begin{aligned}
 \sum_{i = 1}^{n} \frac{(x_i - x_{i-1})}{2} (y_i + y_{i-1})
\end{aligned}

i=1∑n​2(xi​−xi−1​)​(yi​+yi−1​)​

When `x` and `y` have the same size, the computation is as described above and no broadcasting is needed.
The broadcasting behavior of this function is as follows when their sizes are different. For both `x`
and `y`, the function computes the difference between consecutive elements along
dimension `dim`. This effectively creates two tensors, x_diff and y_diff, that have
the same shape as the original tensors except their lengths along the dimension `dim` is reduced by 1.
After that, those two tensors are broadcast together to compute final output as part of the trapezoidal rule.
See the examples below for details.

Note

The trapezoidal rule is a technique for approximating the definite integral of a function
by averaging its left and right Riemann sums. The approximation becomes more accurate as
the resolution of the partition increases.

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
>>> # Computes the trapezoidal rule in 1D, spacing is implicitly 1
>>> y = torch.tensor([1, 5, 10])
>>> torch.trapezoid(y)
tensor(10.5)

>>> # Computes the same trapezoidal rule directly to verify
>>> (1 + 10 + 10) / 2
10.5

>>> # Computes the trapezoidal rule in 1D with constant spacing of 2
>>> # NOTE: the result is the same as before, but multiplied by 2
>>> torch.trapezoid(y, dx=2)
21.0

>>> # Computes the trapezoidal rule in 1D with arbitrary spacing
>>> x = torch.tensor([1, 3, 6])
>>> torch.trapezoid(y, x)
28.5

>>> # Computes the same trapezoidal rule directly to verify
>>> ((3 - 1) * (1 + 5) + (6 - 3) * (5 + 10)) / 2
28.5

>>> # Computes the trapezoidal rule for each row of a 3x3 matrix
>>> y = torch.arange(9).reshape(3, 3)
tensor([[0, 1, 2],
 [3, 4, 5],
 [6, 7, 8]])
>>> torch.trapezoid(y)
tensor([ 2., 8., 14.])

>>> # Computes the trapezoidal rule for each column of the matrix
>>> torch.trapezoid(y, dim=0)
tensor([ 6., 8., 10.])

>>> # Computes the trapezoidal rule for each row of a 3x3 ones matrix
>>> # with the same arbitrary spacing
>>> y = torch.ones(3, 3)
>>> x = torch.tensor([1, 3, 6])
>>> torch.trapezoid(y, x)
array([5., 5., 5.])

>>> # Computes the trapezoidal rule for each row of a 3x3 ones matrix
>>> # with different arbitrary spacing per row
>>> y = torch.ones(3, 3)
>>> x = torch.tensor([[1, 2, 3], [1, 3, 5], [1, 4, 7]])
>>> torch.trapezoid(y, x)
array([2., 4., 6.])
```