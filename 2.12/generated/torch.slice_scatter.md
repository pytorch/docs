# torch.slice_scatter

torch.slice_scatter(*input*, *src*, *dim=0*, *start=None*, *end=None*, *step=1*) → [Tensor](../tensors.html#torch.Tensor)

Embeds the values of the `src` tensor into `input` at the given
dimension.
This function returns a tensor with fresh storage; it does not create a view.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **src** ([*Tensor*](../tensors.html#torch.Tensor)) - The tensor to embed into `input`
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to insert the slice into
- **start** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the start index of where to insert the slice
- **end** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - the end index of where to insert the slice
- **step** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the how many elements to skip in

Example:

```
>>> a = torch.zeros(8, 8)
>>> b = torch.ones(2, 8)
>>> a.slice_scatter(b, start=6)
tensor([[0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0.],
 [1., 1., 1., 1., 1., 1., 1., 1.],
 [1., 1., 1., 1., 1., 1., 1., 1.]])

>>> b = torch.ones(8, 2)
>>> a.slice_scatter(b, dim=1, start=2, end=6, step=2)
tensor([[0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.],
 [0., 0., 1., 0., 1., 0., 0., 0.]])
```