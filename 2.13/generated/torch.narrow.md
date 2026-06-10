# torch.narrow

torch.narrow(*input*, *dim*, *start*, *length*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor that is a narrowed version of `input` tensor. The
dimension `dim` is input from `start` to `start + length`. The
returned tensor and `input` tensor share the same underlying storage.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to narrow
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension along which to narrow
- **start** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*Tensor*](../tensors.html#torch.Tensor)) - index of the element to start the narrowed dimension
from. Can be negative, which means indexing from the end of dim. If
Tensor, it must be an 0-dim integral Tensor (bools not allowed)
- **length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - length of the narrowed dimension, must be weakly positive

Example:

```
>>> x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> torch.narrow(x, 0, 0, 2)
tensor([[ 1, 2, 3],
 [ 4, 5, 6]])
>>> torch.narrow(x, 1, 1, 2)
tensor([[ 2, 3],
 [ 5, 6],
 [ 8, 9]])
>>> torch.narrow(x, -1, torch.tensor(-1), 1)
tensor([[3],
 [6],
 [9]])
```