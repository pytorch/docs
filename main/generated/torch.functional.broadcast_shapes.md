# torch.functional.broadcast_shapes

torch.functional.broadcast_shapes(**shapes*) → [Size](../size.html#torch.Size)[[source]](https://github.com/pytorch/pytorch/blob/09c9b1ec9c2e88520d11a9c64b206359e8ca912b/torch/functional.py#L80)

Similar to [`broadcast_tensors()`](torch.functional.broadcast_tensors.html#torch.functional.broadcast_tensors) but for shapes.

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