# torch.linalg.matrix_power

torch.linalg.matrix_power(*A*, *n*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/linalg/__init__.py#L1202)

Computes the n-th power of a square matrix for an integer n.

Supports input of float, double, cfloat and cdouble dtypes.
Also supports batches of matrices, and if `A` is a batch of matrices then
the output has the same batch dimensions.

If `n`= 0, it returns the identity matrix (or batch) of the same shape
as `A`. If `n` is negative, it returns the inverse of each matrix
(if invertible) raised to the power of abs(n).

Note

Consider using [`torch.linalg.solve()`](torch.linalg.solve.html#torch.linalg.solve) if possible for multiplying a matrix on the left by
a negative power as, if `n`> 0:

```
torch.linalg.solve(matrix_power(A, n), B) == matrix_power(A, -n) @ B
```

It is always preferred to use [`solve()`](torch.linalg.solve.html#torch.linalg.solve) when possible, as it is faster and more
numerically stable than computing A−nA^{-n}A−n explicitly.

See also

[`torch.linalg.solve()`](torch.linalg.solve.html#torch.linalg.solve) computes `A`.inverse() @ `B` with a
numerically stable algorithm.

Parameters:

- **A** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor of shape (*, m, m) where * is zero or more batch dimensions.
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the exponent.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - output tensor. Ignored if None. Default: None.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - if `n`< 0 and the matrix `A` or any matrix in the
 batch of matrices `A` is not invertible.

Examples:

```
>>> A = torch.randn(3, 3)
>>> torch.linalg.matrix_power(A, 0)
tensor([[1., 0., 0.],
 [0., 1., 0.],
 [0., 0., 1.]])
>>> torch.linalg.matrix_power(A, 3)
tensor([[ 1.0756, 0.4980, 0.0100],
 [-1.6617, 1.4994, -1.9980],
 [-0.4509, 0.2731, 0.8001]])
>>> torch.linalg.matrix_power(A.expand(2, -1, -1), -2)
tensor([[[ 0.2640, 0.4571, -0.5511],
 [-1.0163, 0.3491, -1.5292],
 [-0.4899, 0.0822, 0.2773]],
 [[ 0.2640, 0.4571, -0.5511],
 [-1.0163, 0.3491, -1.5292],
 [-0.4899, 0.0822, 0.2773]]])
```