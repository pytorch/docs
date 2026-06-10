# torch.select_scatter

torch.select_scatter(*input*, *src*, *dim*, *index*) → [Tensor](../tensors.html#torch.Tensor)

Embeds the values of the `src` tensor into `input` at the given index.
This function returns a tensor with fresh storage; it does not create a view.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - The tensor to embed into `input`
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to insert the slice into.
- **index** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the index to select with

Note

`src` must be of the proper size in order to be embedded
into `input`. Specifically, it should have the same shape as
`torch.select(input, dim, index)`

Example:

```
>>> a = torch.zeros(2, 2)
>>> b = torch.ones(2)
>>> a.select_scatter(b, 0, 0)
tensor([[1., 1.],
 [0., 0.]])
```