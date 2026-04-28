# torch.nanmean

torch.nanmean(*input*, *dim=None*, *keepdim=False*, ***, *dtype=None*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the mean of all non-NaN elements along the specified dimensions.
Input must be floating point or complex.

This function is identical to [`torch.mean()`](torch.mean.html#torch.mean) when there are no NaN values
in the `input` tensor. In the presence of NaN, [`torch.mean()`](torch.mean.html#torch.mean) will
propagate the NaN to the output whereas `torch.nanmean()` will ignore the
NaN values (torch.nanmean(a) is equivalent to torch.mean(a[~a.isnan()])).

If `keepdim` is `True`, the output tensor is of the same size
as `input` except in the dimension(s) `dim` where it is of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the
output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor, either of floating point or complex dtype
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints**,**optional*) - the dimension or dimensions to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

See also

[`torch.mean()`](torch.mean.html#torch.mean) computes the mean value, propagating NaN.

Example:

```
>>> x = torch.tensor([[torch.nan, 1, 2], [1, 2, 3]])
>>> x.mean()
tensor(nan)
>>> x.nanmean()
tensor(1.8000)
>>> x.mean(dim=0)
tensor([ nan, 1.5000, 2.5000])
>>> x.nanmean(dim=0)
tensor([1.0000, 1.5000, 2.5000])

# If all elements in the reduced dimensions are NaN then the result is NaN
>>> torch.tensor([torch.nan]).nanmean()
tensor(nan)
```