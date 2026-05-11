# torch.nanquantile

torch.nanquantile(*input*, *q*, *dim=None*, *keepdim=False*, ***, *interpolation='linear'*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

This is a variant of [`torch.quantile()`](torch.quantile.html#torch.quantile) that "ignores" `NaN` values,
computing the quantiles `q` as if `NaN` values in `input` did
not exist. If all values in a reduced row are `NaN` then the quantiles for
that reduction will be `NaN`. See the documentation for [`torch.quantile()`](torch.quantile.html#torch.quantile).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **q** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - a scalar or 1D tensor of quantile values in the range [0, 1]
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

- **interpolation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - interpolation method to use when the desired quantile lies between two data points.
Can be `linear`, `lower`, `higher`, `midpoint` and `nearest`.
Default is `linear`.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> t = torch.tensor([float('nan'), 1, 2])
>>> t.quantile(0.5)
tensor(nan)
>>> t.nanquantile(0.5)
tensor(1.5000)
>>> t = torch.tensor([[float('nan'), float('nan')], [1, 2]])
>>> t
tensor([[nan, nan],
 [1., 2.]])
>>> t.nanquantile(0.5, dim=0)
tensor([1., 2.])
>>> t.nanquantile(0.5, dim=1)
tensor([ nan, 1.5000])
```