# torch.Tensor.scatter_add_

Tensor.scatter_add_(*dim*, *index*, *src*) → [Tensor](../tensors.html#torch.Tensor)

Adds all values from the tensor `src` into `self` at the indices
specified in the `index` tensor in a similar fashion as
[`scatter_()`](torch.Tensor.scatter_.html#torch.Tensor.scatter_). For each value in `src`, it is added to
an index in `self` which is specified by its index in `src`
for `dimension != dim` and by the corresponding value in `index` for
`dimension = dim`.

For a 3-D tensor, `self` is updated as:

```
self[index[i][j][k]][j][k] += src[i][j][k] # if dim == 0
self[i][index[i][j][k]][k] += src[i][j][k] # if dim == 1
self[i][j][index[i][j][k]] += src[i][j][k] # if dim == 2
```

`self`, `index` and `src` should have same number of
dimensions. It is also required that `index.size(d) <= src.size(d)` for all
dimensions `d`, and that `index.size(d) <= self.size(d)` for all dimensions
`d != dim`. Note that `index` and `src` do not broadcast.
When `index` is empty, we always return the original tensor
without further error checking.

Note

This operation may behave nondeterministically when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

Note

The backward pass is implemented only for `src.shape == index.shape`.

Parameters:

- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the axis along which to index
- **index** (*LongTensor*) - the indices of elements to scatter and add, can be
either empty or of the same dimensionality as `src`. When empty, the
operation returns `self` unchanged.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the source elements to scatter and add

Example:

```
>>> src = torch.ones((2, 5))
>>> index = torch.tensor([[0, 1, 2, 0, 0]])
>>> torch.zeros(3, 5, dtype=src.dtype).scatter_add_(0, index, src)
tensor([[1., 0., 0., 1., 1.],
 [0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 0.]])
>>> index = torch.tensor([[0, 1, 2, 0, 0], [0, 1, 2, 2, 2]])
>>> torch.zeros(3, 5, dtype=src.dtype).scatter_add_(0, index, src)
tensor([[2., 0., 0., 1., 1.],
 [0., 2., 0., 0., 0.],
 [0., 0., 2., 1., 1.]])
```