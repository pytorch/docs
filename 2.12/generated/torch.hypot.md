# torch.hypot

torch.hypot(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Given the legs of a right triangle, return its hypotenuse.

outi=inputi2+otheri2\text{out}_{i} = \sqrt{\text{input}_{i}^{2} + \text{other}_{i}^{2}}

outi​=inputi2​+otheri2​​

The shapes of `input` and `other` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the first input tensor
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.hypot(torch.tensor([4.0]), torch.tensor([3.0, 4.0, 5.0]))
tensor([5.0000, 5.6569, 6.4031])
```