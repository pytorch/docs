# torch.mode

torch.mode(*input*, *dim=-1*, *keepdim=False*, ***, *out=None*)

Returns a namedtuple `(values, indices)` where `values` is the mode
value of each row of the `input` tensor in the given dimension
`dim`, i.e. a value which appears most often
in that row, and `indices` is the index location of each mode value found.

By default, `dim` is the last dimension of the `input` tensor.

If `keepdim` is `True`, the output tensors are of the same size as
`input` except in the dimension `dim` where they are of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting
in the output tensors having 1 fewer dimension than `input`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to reduce.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - the result tuple of two output tensors (values, indices)

Example:

```
>>> b = torch.tensor([[0, 0, 0, 2, 0, 0, 2],
... [0, 3, 0, 0, 2, 0, 1],
... [2, 2, 2, 0, 0, 0, 3],
... [2, 2, 3, 0, 1, 1, 0],
... [1, 1, 0, 0, 2, 0, 2]])
>>> torch.mode(b, 0)
torch.return_types.mode(
values=tensor([0, 2, 0, 0, 0, 0, 2]),
indices=tensor([1, 3, 4, 4, 2, 4, 4]))
```