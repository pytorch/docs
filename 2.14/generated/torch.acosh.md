# torch.acosh

torch.acosh(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the inverse hyperbolic cosine of the elements of `input`.

outi=cosh⁡−1(inputi)\text{out}_{i} = \cosh^{-1}(\text{input}_{i})

outi​=cosh−1(inputi​)

Note

The domain of the inverse hyperbolic cosine is [1, inf) and values outside this range
will be mapped to `NaN`, except for + INF for which the output is mapped to + INF.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4).uniform_(1, 2)
>>> a
tensor([ 1.3192, 1.9915, 1.9674, 1.7151 ])
>>> torch.acosh(a)
tensor([ 0.7791, 1.3120, 1.2979, 1.1341 ])
```