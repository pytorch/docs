# torch.broadcast_shapes

torch.broadcast_shapes(**shapes*) → [Size](../size.html#torch.Size)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/functional.py#L79)

Similar to [`broadcast_tensors()`](torch.broadcast_tensors.html#torch.broadcast_tensors) but for shapes.

This is equivalent to
`torch.broadcast_tensors(*map(torch.empty, shapes))[0].shape`
but avoids the need to create intermediate tensors. This is useful for
broadcasting tensors of common batch shape but different rightmost shape,
e.g. to broadcast mean vectors with covariance matrices.

Example:

```
>>> torch.broadcast_shapes((2,), (3, 1), (1, 1, 1))
torch.Size([1, 3, 2])
```

Parameters:

***shapes** ([*torch.Size*](../size.html#torch.Size)) - Shapes of tensors.

Returns:

A shape compatible with all input shapes.

Return type:

shape ([torch.Size](../size.html#torch.Size))

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If shapes are incompatible.