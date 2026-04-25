# torch.vsplit

torch.vsplit(*input*, *indices_or_sections*) → List of Tensors

Splits `input`, a tensor with two or more dimensions, into multiple tensors
vertically according to `indices_or_sections`. Each split is a view of
`input`.

This is equivalent to calling torch.tensor_split(input, indices_or_sections, dim=0)
(the split dimension is 0), except that if `indices_or_sections` is an integer
it must evenly divide the split dimension or a runtime error will be thrown.

This function is based on NumPy's [`numpy.vsplit()`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - tensor to split.
- **indices_or_sections** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints*) - See argument in [`torch.tensor_split()`](torch.tensor_split.html#torch.tensor_split).

Example:

```
>>> t = torch.arange(16.0).reshape(4,4)
>>> t
tensor([[ 0., 1., 2., 3.],
 [ 4., 5., 6., 7.],
 [ 8., 9., 10., 11.],
 [12., 13., 14., 15.]])
>>> torch.vsplit(t, 2)
(tensor([[0., 1., 2., 3.],
 [4., 5., 6., 7.]]),
 tensor([[ 8., 9., 10., 11.],
 [12., 13., 14., 15.]]))
>>> torch.vsplit(t, [3, 6])
(tensor([[ 0., 1., 2., 3.],
 [ 4., 5., 6., 7.],
 [ 8., 9., 10., 11.]]),
 tensor([[12., 13., 14., 15.]]),
 tensor([], size=(0, 4)))
```