# torch.as_strided_scatter

torch.as_strided_scatter(*input*, *src*, *size*, *stride*, *storage_offset=None*) → [Tensor](../tensors.html#torch.Tensor)

Embeds the values of the `src` tensor into `input` along
the elements corresponding to the result of calling
input.as_strided(size, stride, storage_offset).

This function returns a tensor with fresh storage; it does not
return a view.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*or**ints*) - the shape of the output tensor
- **stride** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*or**ints*) - the stride of the output tensor
- **storage_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the offset in the underlying storage of the output tensor

Note

`src` must be of the proper size in order to be embedded
into `input`. Specifically, it should have the same shape as
torch.as_strided(input, size, stride, storage_offset)

Example:

```
>>> a = torch.arange(4).reshape(2, 2) + 1
>>> a
tensor([[1, 2],
 [3, 4]])
>>> b = torch.zeros(3, 3)
>>> b
tensor([[0., 0., 0.],
 [0., 0., 0.],
 [0., 0., 0.]])
>>> torch.as_strided_scatter(b, a, (2, 2), (1, 2))
tensor([[1., 3., 2.],
 [4., 0., 0.],
 [0., 0., 0.]])
```