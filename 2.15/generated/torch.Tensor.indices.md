# torch.Tensor.indices

Tensor.indices() → [Tensor](../tensors.html#torch.Tensor)

Return the indices tensor of a [sparse COO tensor](../sparse.html#sparse-coo-docs).

Warning

Throws an error if `self` is not a sparse COO tensor.

See also [`Tensor.values()`](torch.Tensor.values.html#torch.Tensor.values).

Note

This method can only be called on a coalesced sparse tensor. See
[`Tensor.coalesce()`](torch.Tensor.coalesce.html#torch.Tensor.coalesce) for details.