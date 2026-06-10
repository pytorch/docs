# torch.diagonal

torch.diagonal(*input*, *offset=0*, *dim1=0*, *dim2=1*) → [Tensor](../tensors.html#torch.Tensor)

Returns a partial view of `input` with the its diagonal elements
with respect to `dim1` and `dim2` appended as a dimension
at the end of the shape.

The argument `offset` controls which diagonal to consider:

- If `offset` = 0, it is the main diagonal.
- If `offset` > 0, it is above the main diagonal.
- If `offset` < 0, it is below the main diagonal.

Applying [`torch.diag_embed()`](torch.diag_embed.html#torch.diag_embed) to the output of this function with
the same arguments yields a diagonal matrix with the diagonal entries
of the input. However, [`torch.diag_embed()`](torch.diag_embed.html#torch.diag_embed) has different default
dimensions, so those need to be explicitly specified.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor. Must be at least 2-dimensional.
- **offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - which diagonal to consider. Default: 0
(main diagonal).
- **dim1** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - first dimension with respect to which to
take diagonal. Default: 0.
- **dim2** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - second dimension with respect to which to
take diagonal. Default: 1.

Note

To take a batch diagonal, pass in dim1=-2, dim2=-1.

Examples:

```
>>> a = torch.randn(3, 3)
>>> a
tensor([[-1.0854, 1.1431, -0.1752],
 [ 0.8536, -0.0905, 0.0360],
 [ 0.6927, -0.3735, -0.4945]])

>>> torch.diagonal(a)
tensor([-1.0854, -0.0905, -0.4945])

>>> torch.diagonal(a, 1)
tensor([ 1.1431, 0.0360])

>>> b = torch.randn(2, 5)
>>> b
tensor([[-1.7948, -1.2731, -0.3181, 2.0200, -1.6745],
 [ 1.8262, -1.5049, 0.4114, 1.0704, -1.2607]])

>>> torch.diagonal(b, 1, 1, 0)
tensor([1.8262])

>>> x = torch.randn(2, 5, 4, 2)
>>> torch.diagonal(x, offset=-1, dim1=1, dim2=2)
tensor([[[-1.2631, 0.3755, -1.5977, -1.8172],
 [-1.1065, 1.0401, -0.2235, -0.7938]],

 [[-1.7325, -0.3081, 0.6166, 0.2335],
 [ 1.0500, 0.7336, -0.3836, -1.1015]]])
```