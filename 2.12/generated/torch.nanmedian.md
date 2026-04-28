# torch.nanmedian

torch.nanmedian(*input*) → [Tensor](../tensors.html#torch.Tensor)

Returns the median of the values in `input`, ignoring `NaN` values.

This function is identical to [`torch.median()`](torch.median.html#torch.median) when there are no `NaN` values in `input`.
When `input` has one or more `NaN` values, [`torch.median()`](torch.median.html#torch.median) will always return `NaN`,
while this function will return the median of the non-`NaN` elements in `input`.
If all the elements in `input` are `NaN` it will also return `NaN`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> a = torch.tensor([1, float('nan'), 3, 2])
>>> a.median()
tensor(nan)
>>> a.nanmedian()
tensor(2.)
```

torch.nanmedian(*input*, *dim=-1*, *keepdim=False*, ***, *out=None*)

Returns a namedtuple `(values, indices)` where `values` contains the median of each row of `input`
in the dimension `dim`, ignoring `NaN` values, and `indices` contains the index of the median values
found in the dimension `dim`.

This function is identical to [`torch.median()`](torch.median.html#torch.median) when there are no `NaN` values in a reduced row. When a reduced row has
one or more `NaN` values, [`torch.median()`](torch.median.html#torch.median) will always reduce it to `NaN`, while this function will reduce it to the
median of the non-`NaN` elements. If all the elements in a reduced row are `NaN` then it will be reduced to `NaN`, too.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**out** (*(*[*Tensor*](../tensors.html#torch.Tensor)*,*[*Tensor*](../tensors.html#torch.Tensor)*)**,**optional*) - The first tensor will be populated with the median values and the second
tensor, which must have dtype long, with their indices in the dimension
`dim` of `input`.

Example:

```
>>> a = torch.tensor([[2, 3, 1], [float('nan'), 1, float('nan')]])
>>> a
tensor([[2., 3., 1.],
 [nan, 1., nan]])
>>> a.median(0)
torch.return_types.median(values=tensor([nan, 1., nan]), indices=tensor([1, 1, 1]))
>>> a.nanmedian(0)
torch.return_types.nanmedian(values=tensor([2., 1., 1.]), indices=tensor([0, 1, 0]))
```