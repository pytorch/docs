# torch.count_nonzero

torch.count_nonzero(*input*, *dim=None*) → [Tensor](../tensors.html#torch.Tensor)

Counts the number of non-zero values in the tensor `input` along the given `dim`.
If no dim is specified then all non-zeros in the tensor are counted.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints**,**optional*) - Dim or tuple of dims along which to count non-zeros.

Example:

```
>>> x = torch.zeros(3,3)
>>> x[torch.randn(3,3) > 0.5] = 1
>>> x
tensor([[0., 1., 1.],
 [0., 0., 0.],
 [0., 0., 1.]])
>>> torch.count_nonzero(x)
tensor(3)
>>> torch.count_nonzero(x, dim=0)
tensor([0, 1, 2])
```