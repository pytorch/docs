# torch.Tensor.reshape_as

Tensor.reshape_as(*other*) → [Tensor](../tensors.html#torch.Tensor)

Returns this tensor as the same shape as `other`.
`self.reshape_as(other)` is equivalent to `self.reshape(other.sizes())`.
This method returns a view if `other.sizes()` is compatible with the current
shape. See [`torch.Tensor.view()`](torch.Tensor.view.html#torch.Tensor.view) on when it is possible to return a view.

Please see [`reshape()`](torch.reshape.html#torch.reshape) for more information about `reshape`.

Parameters:

**other** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - The result tensor has the same shape
as `other`.