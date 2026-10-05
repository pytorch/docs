# torch.vstack

torch.vstack(*tensors*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Stack tensors in sequence vertically (row wise).

This is equivalent to concatenation along the first axis after all 1-D tensors have been reshaped by [`torch.atleast_2d()`](torch.atleast_2d.html#torch.atleast_2d).

Parameters:

**tensors** (*sequence**of**Tensors*) - sequence of tensors to concatenate

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([1, 2, 3])
>>> b = torch.tensor([4, 5, 6])
>>> torch.vstack((a,b))
tensor([[1, 2, 3],
 [4, 5, 6]])
>>> a = torch.tensor([[1],[2],[3]])
>>> b = torch.tensor([[4],[5],[6]])
>>> torch.vstack((a,b))
tensor([[1],
 [2],
 [3],
 [4],
 [5],
 [6]])
```