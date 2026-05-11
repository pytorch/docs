# torch.asin

torch.asin(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the arcsine of the elements (in radians) in the `input` tensor.

outi=sin⁡−1(inputi)\text{out}_{i} = \sin^{-1}(\text{input}_{i})

outi​=sin−1(inputi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([-0.5962, 1.4985, -0.4396, 1.4525])
>>> torch.asin(a)
tensor([-0.6387, nan, -0.4552, nan])
```