# torch.histogram

torch.histogram(*input*, *bins*, ***, *range=None*, *weight=None*, *density=False*, *out=None*)

Computes a histogram of the values in a tensor.

`bins` can be an integer or a 1D tensor.

If `bins` is an int, it specifies the number of equal-width bins.
By default, the lower and upper range of the bins is determined by the
minimum and maximum elements of the input tensor. The [`range`](torch.range.html#torch.range)
argument can be provided to specify a range for the bins.

If `bins` is a 1D tensor, it specifies the sequence of bin edges
including the rightmost edge. It should contain at least 2 elements
and its elements should be increasing.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **bins** - int or 1D Tensor. If int, defines the number of equal-width bins. If tensor,
defines the sequence of bin edges including the rightmost edge.

Keyword Arguments:

- **range** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*float*](https://docs.python.org/3/library/functions.html#float)) - Defines the range of the bins.
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - If provided, weight should have the same shape as input. Each value in
input contributes its associated weight towards its bin's result.
- **density** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If False, the result will contain the count (or total weight) in each bin.
If True, the result is the value of the probability density function over the bins,
normalized such that the integral over the range of the bins is 1.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor. (tuple, optional): The result tuple of two output tensors (hist, bin_edges).

Returns:

1D Tensor containing the values of the histogram.
bin_edges(Tensor): 1D Tensor containing the edges of the histogram bins.

Return type:

hist ([Tensor](../tensors.html#torch.Tensor))

Example:

```
>>> torch.histogram(torch.tensor([1., 2, 1]), bins=4, range=(0., 3.), weight=torch.tensor([1., 2., 4.]))
(tensor([ 0., 5., 2., 0.]), tensor([0., 0.75, 1.5, 2.25, 3.]))
>>> torch.histogram(torch.tensor([1., 2, 1]), bins=4, range=(0., 3.), weight=torch.tensor([1., 2., 4.]), density=True)
(tensor([ 0., 0.9524, 0.3810, 0.]), tensor([0., 0.75, 1.5, 2.25, 3.]))
```