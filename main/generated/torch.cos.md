# torch.cos

torch.cos(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the cosine of the elements of `input` given in radians.

outi=cos⁡(inputi)\text{out}_{i} = \cos(\text{input}_{i})

outi​=cos(inputi​)
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([ 1.4309, 1.2706, -0.8562, 0.9796])
>>> torch.cos(a)
tensor([ 0.1395, 0.2957, 0.6553, 0.5574])
```