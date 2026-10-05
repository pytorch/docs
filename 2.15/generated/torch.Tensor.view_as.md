# torch.Tensor.view_as

Tensor.view_as(*other*) → [Tensor](../tensors.html#torch.Tensor)

View this tensor as the same size as `other`.
`self.view_as(other)` is equivalent to `self.view(other.size())`.

Please see [`view()`](torch.Tensor.view.html#torch.Tensor.view) for more information about `view`.

Parameters:

**other** ([`torch.Tensor`](../tensors.html#torch.Tensor)) - The result tensor has the same size
as `other`.