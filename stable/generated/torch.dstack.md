# torch.dstack

torch.dstack(*tensors*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Stack tensors in sequence depthwise (along third axis).

This is equivalent to concatenation along the third axis after 1-D and 2-D tensors have been reshaped by [`torch.atleast_3d()`](torch.atleast_3d.html#torch.atleast_3d).

Parameters:

**tensors** (*sequence**of**Tensors*) - sequence of tensors to concatenate

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([1, 2, 3])
>>> b = torch.tensor([4, 5, 6])
>>> torch.dstack((a,b))
tensor([[[1, 4],
 [2, 5],
 [3, 6]]])
>>> a = torch.tensor([[1],[2],[3]])
>>> b = torch.tensor([[4],[5],[6]])
>>> torch.dstack((a,b))
tensor([[[1, 4]],
 [[2, 5]],
 [[3, 6]]])
```