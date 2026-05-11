# torch.unsqueeze

torch.unsqueeze(*input*, *dim*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new tensor with a dimension of size one inserted at the
specified position.

The returned tensor shares the same underlying data with this tensor.

A `dim` value within the range `[-input.dim() - 1, input.dim() + 1)`
can be used. Negative `dim` will correspond to `unsqueeze()`
applied at `dim` = `dim + input.dim() + 1`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the index at which to insert the singleton dimension

Example:

```
>>> x = torch.tensor([1, 2, 3, 4])
>>> torch.unsqueeze(x, 0)
tensor([[ 1, 2, 3, 4]])
>>> torch.unsqueeze(x, 1)
tensor([[ 1],
 [ 2],
 [ 3],
 [ 4]])
```