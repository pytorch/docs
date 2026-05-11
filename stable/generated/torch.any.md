# torch.any

torch.any(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *out: [Tensor](../tensors.html#torch.Tensor) | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Tests if any element in `input` evaluates to True.

Note

This function matches the behaviour of NumPy in returning
output of dtype bool for all supported dtypes except uint8.
For uint8 the dtype of output is uint8 itself.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.rand(1, 2).bool()
>>> a
tensor([[False, True]], dtype=torch.bool)
>>> torch.any(a)
tensor(True, dtype=torch.bool)
>>> a = torch.arange(0, 3)
>>> a
tensor([0, 1, 2])
>>> torch.any(a)
tensor(True)
```

torch.any(*input*, *dim*, *keepdim=False*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

For each row of `input` in the given dimension `dim`,
returns True if any element in the row evaluate to True and False otherwise.

If `keepdim` is `True`, the output tensor is of the same size
as `input` except in the dimension(s) `dim` where it is of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in the
output tensor having 1 (or `len(dim)`) fewer dimension(s).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*or*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of**ints**,**optional*) - the dimension or dimensions to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(4, 2) < 0
>>> a
tensor([[ True, True],
 [False, True],
 [ True, True],
 [False, False]])
>>> torch.any(a, 1)
tensor([ True, True, True, False])
>>> torch.any(a, 0)
tensor([True, True])
```