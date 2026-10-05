# torch.maximum

torch.maximum(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Computes the element-wise maximum of `input` and `other`.

Note

If one of the elements being compared is a NaN, then that element is returned.
`maximum()` is not supported for tensors with complex dtypes.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **other** ([*Tensor*](../tensors.html#torch.Tensor)) - the second input tensor

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.tensor((1, 2, -1))
>>> b = torch.tensor((3, 0, 4))
>>> torch.maximum(a, b)
tensor([3, 2, 4])
```