# torch.atan2

torch.atan2(*input: [Tensor](../tensors.html#torch.Tensor)*, *other: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Element-wise arctangent of inputi/otheri\text{input}_{i} / \text{other}_{i}inputi​/otheri​
with consideration of the quadrant. Returns a new tensor with the signed angles
in radians between vector (otheri,inputi)(\text{other}_{i}, \text{input}_{i})(otheri​,inputi​)
and vector (1,0)(1, 0)(1,0). (Note that otheri\text{other}_{i}otheri​, the second
parameter, is the x-coordinate, while inputi\text{input}_{i}inputi​, the first
parameter, is the y-coordinate.)

The shapes of `input` and `other` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the first input tensor
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4)
>>> a
tensor([ 0.9041, 0.0196, -0.3108, -2.4423])
>>> torch.atan2(a, torch.randn(4))
tensor([ 0.9833, 0.0811, -1.9743, -1.4151])
```