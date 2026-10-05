# torch.Tensor.coalesce

Tensor.coalesce() → [Tensor](../tensors.html#torch.Tensor)

Returns a coalesced copy of `self` if `self` is an
[uncoalesced tensor](../sparse.html#sparse-uncoalesced-coo-docs).

Returns `self` if `self` is a coalesced tensor.

Warning

Throws an error if `self` is not a sparse COO tensor.