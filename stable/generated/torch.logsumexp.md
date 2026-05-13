# torch.logsumexp

torch.logsumexp(*input*, *dim*, *keepdim=False*, ***, *out=None*)

Returns the log of summed exponentials of each row of the `input`
tensor in the given dimension `dim`. The computation is numerically
stabilized.

For summation index jjj given by dim and other indices iii, the result is

> logsumexp(x)i=log⁡∑jexp⁡(xij)\text{logsumexp}(x)_{i} = \log \sum_j \exp(x_{ij})
> 
> logsumexp(x)i​=logj∑​exp(xij​)

If `keepdim` is `True`, the output tensor is of the same size
as `input` except in the dimension(s) `dim` where it is of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the
output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints*) - the dimension or dimensions to reduce.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(3, 3)
>>> torch.logsumexp(a, 1)
tensor([1.4907, 1.0593, 1.5696])
>>> torch.dist(torch.logsumexp(a, 1), torch.log(torch.sum(torch.exp(a), 1)))
tensor(1.6859e-07)
```