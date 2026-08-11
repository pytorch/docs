# torch.broadcast_to

torch.broadcast_to(*input*, *shape*) → [Tensor](../tensors.html#torch.Tensor)

Broadcasts `input` to the shape `shape`.
Equivalent to calling `input.expand(shape)`. See [`expand()`](torch.Tensor.expand.html#torch.Tensor.expand) for details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **shape** (list, tuple, or [`torch.Size`](../size.html#torch.Size)) - the new shape.

Example:

```
>>> x = torch.tensor([1, 2, 3])
>>> torch.broadcast_to(x, (3, 3))
tensor([[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]])
```