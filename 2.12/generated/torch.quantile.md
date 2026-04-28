# torch.quantile

torch.quantile(*input*, *q*, *dim=None*, *keepdim=False*, ***, *interpolation='linear'*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the q-th quantiles of each row of the `input` tensor along the dimension `dim`.

To compute the quantile, we map q in [0, 1] to the range of indices [0, n] to find the location
of the quantile in the sorted input. If the quantile lies between two data points `a < b` with
indices `i` and `j` in the sorted order, result is computed according to the given
`interpolation` method as follows:

- `linear`: `a + (b - a) * fraction`, where `fraction` is the fractional part of the computed quantile index.
- `lower`: `a`.
- `higher`: `b`.
- `nearest`: `a` or `b`, whichever's index is closer to the computed quantile index (follows [`torch.round()`](torch.round.html#torch.round)).
- `midpoint`: `(a + b) / 2`.

If `q` is a 1D tensor, the first dimension of the output represents the quantiles and has size
equal to the size of `q`, the remaining dimensions are what remains from the reduction.

Note

By default `dim` is `None` resulting in the `input` tensor being flattened before computation.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **q** ([*float*](https://docs.python.org/3/library/functions.html#float)*or*[*Tensor*](../tensors.html#torch.Tensor)) - a scalar or 1D tensor of values in the range [0, 1].
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to reduce.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

- **interpolation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - interpolation method to use when the desired quantile lies between two data points.
Can be `linear`, `lower`, `higher`, `midpoint` and `nearest`.
Default is `linear`.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(2, 3)
>>> a
tensor([[ 0.0795, -1.2117, 0.9765],
 [ 1.1707, 0.6706, 0.4884]])
>>> q = torch.tensor([0.25, 0.5, 0.75])
>>> torch.quantile(a, q, dim=1, keepdim=True)
tensor([[[-0.5661],
 [ 0.5795]],

 [[ 0.0795],
 [ 0.6706]],

 [[ 0.5280],
 [ 0.9206]]])
>>> torch.quantile(a, q, dim=1, keepdim=True).shape
torch.Size([3, 2, 1])
>>> a = torch.arange(4.)
>>> a
tensor([0., 1., 2., 3.])
>>> torch.quantile(a, 0.6, interpolation='linear')
tensor(1.8000)
>>> torch.quantile(a, 0.6, interpolation='lower')
tensor(1.)
>>> torch.quantile(a, 0.6, interpolation='higher')
tensor(2.)
>>> torch.quantile(a, 0.6, interpolation='midpoint')
tensor(1.5000)
>>> torch.quantile(a, 0.6, interpolation='nearest')
tensor(2.)
>>> torch.quantile(a, 0.4, interpolation='nearest')
tensor(1.)
```