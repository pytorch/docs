# torch.Tensor.requires_grad

Tensor.requires_grad

Is `True` if gradients need to be computed for this Tensor, `False` otherwise.

Note

The fact that gradients need to be computed for a Tensor do not mean that the [`grad`](torch.Tensor.grad.html#torch.Tensor.grad)
attribute will be populated, see [`is_leaf`](torch.Tensor.is_leaf.html#torch.Tensor.is_leaf) for more details.