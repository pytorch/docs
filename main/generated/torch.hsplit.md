# torch.hsplit

torch.hsplit(*input*, *indices_or_sections*) → List of Tensors

Splits `input`, a tensor with one or more dimensions, into multiple tensors
horizontally according to `indices_or_sections`. Each split is a view of
`input`.

If `input` is one dimensional this is equivalent to calling
torch.tensor_split(input, indices_or_sections, dim=0) (the split dimension is
zero), and if `input` has two or more dimensions it's equivalent to calling
torch.tensor_split(input, indices_or_sections, dim=1) (the split dimension is 1),
except that if `indices_or_sections` is an integer it must evenly divide
the split dimension or a runtime error will be thrown.

This function is based on NumPy's [`numpy.hsplit()`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit).

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
>>> torch.hsplit(t, 2)
(tensor([[ 0., 1.],
 [ 4., 5.],
 [ 8., 9.],
 [12., 13.]]),
 tensor([[ 2., 3.],
 [ 6., 7.],
 [10., 11.],
 [14., 15.]]))
>>> torch.hsplit(t, [3, 6])
(tensor([[ 0., 1., 2.],
 [ 4., 5., 6.],
 [ 8., 9., 10.],
 [12., 13., 14.]]),
 tensor([[ 3.],
 [ 7.],
 [11.],
 [15.]]),
 tensor([], size=(4, 0)))
```