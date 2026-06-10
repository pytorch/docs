# torch.histc

torch.histc(*input*, *bins=100*, *min=0*, *max=0*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the histogram of a tensor.

The elements are sorted into equal width bins between [`min`](torch.min.html#torch.min) and
[`max`](torch.max.html#torch.max). If [`min`](torch.min.html#torch.min) and [`max`](torch.max.html#torch.max) are both zero, the minimum and
maximum values of the data are used.

Elements lower than min and higher than max and `NaN` elements are ignored.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **bins** ([*int*](https://docs.python.org/3/library/functions.html#int)) - number of histogram bins
- **min** (*Scalar*) - lower end of the range (inclusive)
- **max** (*Scalar*) - upper end of the range (inclusive)

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Returns:

Histogram represented as a tensor

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> torch.histc(torch.tensor([1., 2, 1]), bins=4, min=0, max=3)
tensor([ 0., 2., 1., 0.])
```