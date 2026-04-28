# torch.msort

torch.msort(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Sorts the elements of the `input` tensor along its first dimension
in ascending order by value.

Note

torch.msort(t) is equivalent to torch.sort(t, dim=0)[0].
See also [`torch.sort()`](torch.sort.html#torch.sort).

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> t = torch.randn(3, 4)
>>> t
tensor([[-0.1321, 0.4370, -1.2631, -1.1289],
 [-2.0527, -1.1250, 0.2275, 0.3077],
 [-0.0881, -0.1259, -0.5495, 1.0284]])
>>> torch.msort(t)
tensor([[-2.0527, -1.1250, -1.2631, -1.1289],
 [-0.1321, -0.1259, -0.5495, 0.3077],
 [-0.0881, 0.4370, 0.2275, 1.0284]])
```