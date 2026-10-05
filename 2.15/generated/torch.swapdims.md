# torch.swapdims

torch.swapdims(*input*, *dim0*, *dim1*) → [Tensor](../tensors.html#torch.Tensor)

Alias for [`torch.transpose()`](torch.transpose.html#torch.transpose).

This function is equivalent to NumPy's swapaxes function.

Examples:

```
>>> x = torch.tensor([[[0,1],[2,3]],[[4,5],[6,7]]])
>>> x
tensor([[[0, 1],
 [2, 3]],

 [[4, 5],
 [6, 7]]])
>>> torch.swapdims(x, 0, 1)
tensor([[[0, 1],
 [4, 5]],

 [[2, 3],
 [6, 7]]])
>>> torch.swapdims(x, 0, 2)
tensor([[[0, 4],
 [2, 6]],

 [[1, 5],
 [3, 7]]])
```