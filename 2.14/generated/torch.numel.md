# torch.numel

torch.numel(*input: [Tensor](../tensors.html#torch.Tensor)*) → [int](https://docs.python.org/3/library/functions.html#int)

Returns the total number of elements in the `input` tensor.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Example:

```
>>> a = torch.randn(1, 2, 3, 4, 5)
>>> torch.numel(a)
120
>>> a = torch.zeros(4,4)
>>> torch.numel(a)
16
```