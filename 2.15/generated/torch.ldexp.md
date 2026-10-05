# torch.ldexp

torch.ldexp(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Multiplies `input` by 2 ** `other`.

outi=inputi∗2iother\text{{out}}_i = \text{{input}}_i * 2^\text{{other}}_i

outi​=inputi​∗2iother​

Typically this function is used to construct floating point numbers by multiplying
mantissas in `input` with integral powers of two created from the exponents
in `other`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - a tensor of exponents, typically integers.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.ldexp(torch.tensor([1.]), torch.tensor([1]))
tensor([2.])
>>> torch.ldexp(torch.tensor([1.0]), torch.tensor([1, 2, 3, 4]))
tensor([ 2., 4., 8., 16.])
```