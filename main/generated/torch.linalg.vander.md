# torch.linalg.vander

torch.linalg.vander(*x*, *N=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/df83f06a8c49a667b9408934fa9eaae1aaf32d04/torch/linalg/__init__.py#L2926)

Generates a Vandermonde matrix.

Returns the Vandermonde matrix VVV

V=(1x1x12...x1N−11x2x22...x2N−11x3x32...x3N−1⋮⋮⋮⋱⋮1xnxn2...xnN−1).V = \begin{pmatrix}
 1 & x_1 & x_1^2 & \dots & x_1^{N-1}\\
 1 & x_2 & x_2^2 & \dots & x_2^{N-1}\\
 1 & x_3 & x_3^2 & \dots & x_3^{N-1}\\
 \vdots & \vdots & \vdots & \ddots &\vdots \\
 1 & x_n & x_n^2 & \dots & x_n^{N-1}
 \end{pmatrix}.V=​111⋮1​x1​x2​x3​⋮xn​​x12​x22​x32​⋮xn2​​.........⋱...​x1N−1​x2N−1​x3N−1​⋮xnN−1​​​.

for N > 1.
If `N`= None, then N = x.size(-1) so that the output is a square matrix.

Supports inputs of float, double, cfloat, cdouble, and integral dtypes.
Also supports batches of vectors, and if `x` is a batch of vectors then
the output has the same batch dimensions.

Differences with numpy.vander:

- Unlike numpy.vander, this function returns the powers of `x` in ascending order.
To get them in the reverse order call `linalg.vander(x, N).flip(-1)`.

Parameters:

**x** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, n) where * is zero or more batch dimensions
consisting of vectors.

Keyword Arguments:

**N** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Number of columns in the output. Default: x.size(-1)

Example:

```
>>> x = torch.tensor([1, 2, 3, 5])
>>> linalg.vander(x)
tensor([[ 1, 1, 1, 1],
 [ 1, 2, 4, 8],
 [ 1, 3, 9, 27],
 [ 1, 5, 25, 125]])
>>> linalg.vander(x, N=3)
tensor([[ 1, 1, 1],
 [ 1, 2, 4],
 [ 1, 3, 9],
 [ 1, 5, 25]])
```