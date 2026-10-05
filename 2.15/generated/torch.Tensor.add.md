# torch.Tensor.add

Tensor.add(*other*, ***, *alpha=1*) → [Tensor](../tensors.html#torch.Tensor)

Add a scalar or tensor to `self` tensor. If both `alpha`
and `other` are specified, each element of `other` is scaled by
`alpha` before being used.

When `other` is a tensor, the shape of `other` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with the shape of the underlying
tensor

See [`torch.add()`](torch.add.html#torch.add)