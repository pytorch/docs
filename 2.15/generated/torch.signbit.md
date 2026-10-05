# torch.signbit

torch.signbit(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Tests if each element of `input` has its sign bit set or not.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([0.7, -1.2, 0., 2.3])
>>> torch.signbit(a)
tensor([ False, True, False, False])
>>> a = torch.tensor([-0.0, 0.0])
>>> torch.signbit(a)
tensor([ True, False])
```

Note

signbit handles signed zeros, so negative zero (-0) returns True.