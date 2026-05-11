# torch.log2

torch.log2(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the logarithm to the base 2 of the elements
of `input`.

yi=log⁡2(xi)y_{i} = \log_{2} (x_{i})

yi​=log2​(xi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.rand(5)
>>> a
tensor([ 0.8419, 0.8003, 0.9971, 0.5287, 0.0490])

>>> torch.log2(a)
tensor([-0.2483, -0.3213, -0.0042, -0.9196, -4.3504])
```