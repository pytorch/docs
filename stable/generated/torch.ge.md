# torch.ge

torch.ge(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes input≥other\text{input} \geq \text{other}input≥other element-wise.

The second argument can be a number or a tensor whose shape is
[broadcastable](../notes/broadcasting.html#broadcasting-semantics) with the first argument.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to compare
- **other** ([*Tensor*](../tensors.html#torch.Tensor)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - the tensor or value to compare

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Returns:

A boolean tensor that is True where `input` is greater than or equal to `other` and False elsewhere

Example:

```
>>> torch.ge(torch.tensor([[1, 2], [3, 4]]), torch.tensor([[1, 1], [4, 4]]))
tensor([[True, True], [False, True]])
```