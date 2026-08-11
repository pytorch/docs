# torch.atanh

torch.atanh(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the inverse hyperbolic tangent of the elements of `input`.

Note

The domain of the inverse hyperbolic tangent is (-1, 1) and values outside this range
will be mapped to `NaN`, except for the values 1 and -1 for which the output is
mapped to +/-INF respectively.

outi=tanh⁡−1(inputi)\text{out}_{i} = \tanh^{-1}(\text{input}_{i})

outi​=tanh−1(inputi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4).uniform_(-1, 1)
>>> a
tensor([ -0.9385, 0.2968, -0.8591, -0.1871 ])
>>> torch.atanh(a)
tensor([ -1.7253, 0.3060, -1.2899, -0.1893 ])
```