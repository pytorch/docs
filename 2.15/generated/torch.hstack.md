# torch.hstack

torch.hstack(*tensors*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Stack tensors in sequence horizontally (column wise).

This is equivalent to concatenation along the first axis for 1-D tensors, and along the second axis for all other tensors.

Parameters:

**tensors** (*sequence**of**Tensors*) - sequence of tensors to concatenate

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor([1, 2, 3])
>>> b = torch.tensor([4, 5, 6])
>>> torch.hstack((a,b))
tensor([1, 2, 3, 4, 5, 6])
>>> a = torch.tensor([[1],[2],[3]])
>>> b = torch.tensor([[4],[5],[6]])
>>> torch.hstack((a,b))
tensor([[1, 4],
 [2, 5],
 [3, 6]])
```