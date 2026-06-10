# torch.asinh

torch.asinh(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the inverse hyperbolic sine of the elements of `input`.

outi=sinh⁡−1(inputi)\text{out}_{i} = \sinh^{-1}(\text{input}_{i})

outi​=sinh−1(inputi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([ 0.1606, -1.4267, -1.0899, -1.0250 ])
>>> torch.asinh(a)
tensor([ 0.1599, -1.1534, -0.9435, -0.8990 ])
```