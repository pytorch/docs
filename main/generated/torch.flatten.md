# torch.flatten

torch.flatten(*input*, *start_dim=0*, *end_dim=-1*) → [Tensor](../tensors.html#torch.Tensor)

Flattens `input` by reshaping it into a one-dimensional tensor. If `start_dim` or `end_dim`
are passed, only dimensions starting with `start_dim` and ending with `end_dim` are flattened.
The order of elements in `input` is unchanged.

Unlike NumPy's flatten, which always copies input's data, this function may return the original object, a view,
or copy. If no dimensions are flattened, then the original object `input` is returned. Otherwise, if input can
be viewed as the flattened shape, then that view is returned. Finally, only if the input cannot be viewed as the
flattened shape is input's data copied. See [`torch.Tensor.view()`](torch.Tensor.view.html#torch.Tensor.view) for details on when a view will be returned.

Note

Flattening a zero-dimensional tensor will return a one-dimensional view.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **start_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the first dim to flatten
- **end_dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the last dim to flatten

Example:

```
>>> t = torch.tensor([[[1, 2],
... [3, 4]],
... [[5, 6],
... [7, 8]]])
>>> torch.flatten(t)
tensor([1, 2, 3, 4, 5, 6, 7, 8])
>>> torch.flatten(t, start_dim=1)
tensor([[1, 2, 3, 4],
 [5, 6, 7, 8]])
```