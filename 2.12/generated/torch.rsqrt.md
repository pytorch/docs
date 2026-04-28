# torch.rsqrt

torch.rsqrt(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the reciprocal of the square-root of each of
the elements of `input`.

outi=1inputi\text{out}_{i} = \frac{1}{\sqrt{\text{input}_{i}}}

outi​=inputi​​1​
Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([-0.0370, 0.2970, 1.5420, -0.9105])
>>> torch.rsqrt(a)
tensor([ nan, 1.8351, 0.8053, nan])
```