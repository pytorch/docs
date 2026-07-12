# torch.functional.broadcast_shapes

torch.functional.broadcast_shapes(**shapes*) → [Size](../size.html#torch.Size)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/functional.py#L79)

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