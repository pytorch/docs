# torch.isneginf

torch.isneginf(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Tests if each element of `input` is negative infinity or not.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([-float('inf'), float('inf'), 1.2])
>>> torch.isneginf(a)
tensor([ True, False, False])
```