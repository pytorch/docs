# torch.diagonal_scatter

torch.diagonal_scatter(*input*, *src*, *offset=0*, *dim1=0*, *dim2=1*) → [Tensor](../tensors.html#torch.Tensor)

Embeds the values of the `src` tensor into `input` along
the diagonal elements of `input`, with respect to `dim1`
and `dim2`.

This function returns a tensor with fresh storage; it does not
return a view.

The argument `offset` controls which diagonal to consider:

- If `offset` = 0, it is the main diagonal.
- If `offset` > 0, it is above the main diagonal.
- If `offset` < 0, it is below the main diagonal.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor. Must be at least 2-dimensional.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to embed into `input`.
- **offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - which diagonal to consider. Default: 0
(main diagonal).
- **dim1** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - first dimension with respect to which to
take diagonal. Default: 0.
- **dim2** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - second dimension with respect to which to
take diagonal. Default: 1.

Note

`src` must be of the proper size in order to be embedded
into `input`. Specifically, it should have the same shape as
`torch.diagonal(input, offset, dim1, dim2)`

Examples:

```
>>> a = torch.zeros(3, 3)
>>> a
tensor([[0., 0., 0.],
 [0., 0., 0.],
 [0., 0., 0.]])

>>> torch.diagonal_scatter(a, torch.ones(3), 0)
tensor([[1., 0., 0.],
 [0., 1., 0.],
 [0., 0., 1.]])

>>> torch.diagonal_scatter(a, torch.ones(2), 1)
tensor([[0., 1., 0.],
 [0., 0., 1.],
 [0., 0., 0.]])
```