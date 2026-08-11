# torch.Tensor.is_coalesced

Tensor.is_coalesced() → [bool](https://docs.python.org/3/library/functions.html#bool)

Returns `True` if `self` is a [sparse COO tensor](../sparse.html#sparse-coo-docs) that is coalesced, `False` otherwise.

Warning

Throws an error if `self` is not a sparse COO tensor.

See [`coalesce()`](torch.Tensor.coalesce.html#torch.Tensor.coalesce) and [uncoalesced tensors](../sparse.html#sparse-uncoalesced-coo-docs).