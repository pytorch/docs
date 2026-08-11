# torch.Tensor.sparse_resize_

Tensor.sparse_resize_(*size*, *sparse_dim*, *dense_dim*) → [Tensor](../tensors.html#torch.Tensor)

Resizes `self` [sparse tensor](../sparse.html#sparse-docs) to the desired
size and the number of sparse and dense dimensions.

Note

If the number of specified elements in `self` is zero, then
[`size`](torch.Tensor.size.html#torch.Tensor.size), [`sparse_dim`](torch.Tensor.sparse_dim.html#torch.Tensor.sparse_dim), and [`dense_dim`](torch.Tensor.dense_dim.html#torch.Tensor.dense_dim) can be any
size and positive integers such that `len(size) == sparse_dim +
dense_dim`.

If `self` specifies one or more elements, however, then each
dimension in [`size`](torch.Tensor.size.html#torch.Tensor.size) must not be smaller than the corresponding
dimension of `self`, [`sparse_dim`](torch.Tensor.sparse_dim.html#torch.Tensor.sparse_dim) must equal the number
of sparse dimensions in `self`, and [`dense_dim`](torch.Tensor.dense_dim.html#torch.Tensor.dense_dim) must
equal the number of dense dimensions in `self`.

Warning

Throws an error if `self` is not a sparse tensor.

Parameters:

- **size** ([*torch.Size*](../size.html#torch.Size)) - the desired size. If `self` is non-empty
sparse tensor, the desired size cannot be smaller than the
original size.
- **sparse_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of sparse dimensions
- **dense_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of dense dimensions