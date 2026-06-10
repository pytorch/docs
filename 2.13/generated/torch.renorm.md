# torch.renorm

torch.renorm(*input*, *p*, *dim*, *maxnorm*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor where each sub-tensor of `input` along dimension
`dim` is normalized such that the p-norm of the sub-tensor is lower
than the value `maxnorm`

Note

If the norm of a row is lower than maxnorm, the row is unchanged

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **p** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the power for the norm computation
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to slice over to get the sub-tensors
- **maxnorm** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the maximum norm to keep each sub-tensor under

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> x = torch.ones(3, 3)
>>> x[1].fill_(2)
tensor([ 2., 2., 2.])
>>> x[2].fill_(3)
tensor([ 3., 3., 3.])
>>> x
tensor([[ 1., 1., 1.],
 [ 2., 2., 2.],
 [ 3., 3., 3.]])
>>> torch.renorm(x, 1, 0, 5)
tensor([[ 1.0000, 1.0000, 1.0000],
 [ 1.6667, 1.6667, 1.6667],
 [ 1.6667, 1.6667, 1.6667]])
```