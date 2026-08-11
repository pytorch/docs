# torch.Tensor.dense_dim

Tensor.dense_dim() → [int](https://docs.python.org/3/library/functions.html#int)

Return the number of dense dimensions in a [sparse tensor](../sparse.html#sparse-docs) `self`.

Note

Returns `len(self.shape)` if `self` is not a sparse tensor.

See also [`Tensor.sparse_dim()`](torch.Tensor.sparse_dim.html#torch.Tensor.sparse_dim) and [hybrid tensors](../sparse.html#sparse-hybrid-coo-docs).