# torch.ravel

torch.ravel(*input*) → [Tensor](../tensors.html#torch.Tensor)

Return a contiguous flattened tensor. A copy is made only if needed.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> t = torch.tensor([[[1, 2],
... [3, 4]],
... [[5, 6],
... [7, 8]]])
>>> torch.ravel(t)
tensor([1, 2, 3, 4, 5, 6, 7, 8])
```