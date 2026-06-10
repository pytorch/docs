# torch.logcumsumexp

torch.logcumsumexp(*input*, *dim*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the logarithm of the cumulative summation of the exponentiation of
elements of `input` in the dimension `dim`.

For summation index jjj given by dim and other indices iii, the result is

> logcumsumexp(x)ij=log⁡∑k=0jexp⁡(xik)\text{logcumsumexp}(x)_{ij} = \log \sum\limits_{k=0}^{j} \exp(x_{ik})
> 
> logcumsumexp(x)ij​=logk=0∑j​exp(xik​)

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to do the operation over

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(10)
>>> torch.logcumsumexp(a, dim=0)
tensor([-0.42296738, -0.04462666, 0.86278635, 0.94622083, 1.05277811,
 1.39202815, 1.83525007, 1.84492621, 2.06084887, 2.06844475]))
```