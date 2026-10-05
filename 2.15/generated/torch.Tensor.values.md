# torch.Tensor.values

Tensor.values() → [Tensor](../tensors.html#torch.Tensor)

Return the values tensor of a [sparse COO tensor](../sparse.html#sparse-coo-docs).

Warning

Throws an error if `self` is not a sparse COO tensor.

See also [`Tensor.indices()`](torch.Tensor.indices.html#torch.Tensor.indices).

Note

This method can only be called on a coalesced sparse tensor. See
[`Tensor.coalesce()`](torch.Tensor.coalesce.html#torch.Tensor.coalesce) for details.