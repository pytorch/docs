# torch.take

torch.take(*input*, *index*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with the elements of `input` at the given indices.
The input tensor is treated as if it were viewed as a 1-D tensor. The result
takes the same shape as the indices.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **index** (*LongTensor*) - the indices into tensor

Example:

```
>>> src = torch.tensor([[4, 3, 5],
... [6, 7, 8]])
>>> torch.take(src, torch.tensor([0, 2, 5]))
tensor([ 4, 5, 8])
```