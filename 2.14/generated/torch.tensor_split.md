# torch.tensor_split

torch.tensor_split(*input*, *indices_or_sections*, *dim=0*) → List of Tensors

Splits a tensor into multiple sub-tensors, all of which are views of `input`,
along dimension `dim` according to the indices or number of sections specified
by `indices_or_sections`. This function is based on NumPy's
[`numpy.array_split()`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split).

torch.tensor_split(*input*, *sections*, *dim=0*) → List of Tensors

Splits `input` into `sections` sections along dimension `dim`.
If `input` is divisible by `sections` along dimension `dim`, each
section will be of equal size, `input.size(dim) / sections`. If `input`
is not divisible by `sections`, the sizes of the first
`int(input.size(dim) % sections)` sections will have size
`int(input.size(dim) / sections) + 1`, and the rest will have size
`int(input.size(dim) / sections)`.

`sections` can also be a zero-dimensional long tensor.

torch.tensor_split(*input*, *indices*, *dim=0*) → List of Tensors

Splits `input` along dimension `dim` at each of the indices in
`indices`. For instance, `indices=[2, 3]` and `dim=0`
would result in the tensors `input[:2]`, `input[2:3]`, and
`input[3:]`.

`indices` can be a list or tuple of ints, or a one-dimensional long
tensor on the CPU.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor to split
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - dimension along which to split the tensor. Default: `0`

Example:

```
>>> x = torch.arange(8)
>>> torch.tensor_split(x, 3)
(tensor([0, 1, 2]), tensor([3, 4, 5]), tensor([6, 7]))

>>> x = torch.arange(7)
>>> torch.tensor_split(x, 3)
(tensor([0, 1, 2]), tensor([3, 4]), tensor([5, 6]))
>>> torch.tensor_split(x, (1, 6))
(tensor([0]), tensor([1, 2, 3, 4, 5]), tensor([6]))

>>> x = torch.arange(14).reshape(2, 7)
>>> x
tensor([[ 0, 1, 2, 3, 4, 5, 6],
 [ 7, 8, 9, 10, 11, 12, 13]])
>>> torch.tensor_split(x, 3, dim=1)
(tensor([[0, 1, 2],
 [7, 8, 9]]),
 tensor([[ 3, 4],
 [10, 11]]),
 tensor([[ 5, 6],
 [12, 13]]))
>>> torch.tensor_split(x, (1, 6), dim=1)
(tensor([[0],
 [7]]),
 tensor([[ 1, 2, 3, 4, 5],
 [ 8, 9, 10, 11, 12]]),
 tensor([[ 6],
 [13]]))
```