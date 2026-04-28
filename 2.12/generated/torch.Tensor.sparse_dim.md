# torch.Tensor.sparse_dim

Tensor.sparse_dim() → [int](https://docs.python.org/3/library/functions.html#int)

Return the number of sparse dimensions in a [sparse tensor](../sparse.html#sparse-docs) `self`.

Note

Returns `0` if `self` is not a sparse tensor.

See also [`Tensor.dense_dim()`](torch.Tensor.dense_dim.html#torch.Tensor.dense_dim) and [hybrid tensors](../sparse.html#sparse-hybrid-coo-docs).