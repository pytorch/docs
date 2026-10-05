# torch.nextafter

torch.nextafter(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Return the next floating-point value after `input` towards `other`, elementwise.

The shapes of `input` and `other` must be
[broadcastable](../notes/broadcasting.html#broadcasting-semantics).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the first input tensor
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> eps = torch.finfo(torch.float32).eps
>>> torch.nextafter(torch.tensor([1.0, 2.0]), torch.tensor([2.0, 1.0])) == torch.tensor([eps + 1, 2 - eps])
tensor([True, True])
```