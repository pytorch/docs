# torch.reciprocal

torch.reciprocal(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the reciprocal of the elements of `input`

outi=1inputi\text{out}_{i} = \frac{1}{\text{input}_{i}}

outi​=inputi​1​

Note

Unlike NumPy's reciprocal, torch.reciprocal supports integral inputs. Integral
inputs to reciprocal are automatically [promoted](../tensor_attributes.html#type-promotion-doc) to
the default scalar type.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([-0.4595, -2.1219, -1.4314, 0.7298])
>>> torch.reciprocal(a)
tensor([-2.1763, -0.4713, -0.6986, 1.3702])
```