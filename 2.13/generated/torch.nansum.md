# torch.nansum

torch.nansum(*input*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the sum of all elements, treating Not a Numbers (NaNs) as zero.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Example:

```
>>> a = torch.tensor([1., 2., float('nan'), 4.])
>>> torch.nansum(a)
tensor(7.)
```

torch.nansum(*input*, *dim*, *keepdim=False*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the sum of each row of the `input` tensor in the given
dimension `dim`, treating Not a Numbers (NaNs) as zero.
If `dim` is a list of dimensions, reduce over all of them.

If `keepdim` is `True`, the output tensor is of the same size
as `input` except in the dimension(s) `dim` where it is of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the
output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints**,**optional*) - the dimension or dimensions to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Example:

```
>>> torch.nansum(torch.tensor([1., float("nan")]))
tensor(1.)
>>> a = torch.tensor([[1, 2], [3., float("nan")]])
>>> torch.nansum(a)
tensor(6.)
>>> torch.nansum(a, dim=0)
tensor([4., 2.])
>>> torch.nansum(a, dim=1)
tensor([3., 3.])
```