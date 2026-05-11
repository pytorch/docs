# torch.bitwise_and

torch.bitwise_and(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the bitwise AND of `input` and `other`. The input tensor must be of
integral or Boolean types. For bool tensors, it computes the logical AND.

Parameters:

- **input** - the first input tensor
- **other** - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> torch.bitwise_and(torch.tensor([-1, -2, 3], dtype=torch.int8), torch.tensor([1, 0, 3], dtype=torch.int8))
tensor([1, 0, 3], dtype=torch.int8)
>>> torch.bitwise_and(torch.tensor([True, True, False]), torch.tensor([False, True, False]))
tensor([ False, True, False])
```