# torch.unbind

torch.unbind(*input*, *dim=0*) → seq

Removes a tensor dimension.

Returns a tuple of all slices along a given dimension, already without it.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to unbind
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - dimension to remove

Example:

```
>>> torch.unbind(torch.tensor([[1, 2, 3],
>>> [4, 5, 6],
>>> [7, 8, 9]]))
(tensor([1, 2, 3]), tensor([4, 5, 6]), tensor([7, 8, 9]))
```