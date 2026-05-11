# torch.sum

torch.sum(*input*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the sum of all elements in the `input` tensor.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Note

Use the dtype argument if you need the result in a specific tensor type.
Otherwise, the result type may be automatically promoted (e.g., from torch.int32 to torch.int64).

Example:

```
>>> a = torch.randn(1, 3)
>>> a
tensor([[ 0.1133, -0.9567, 0.2958]])
>>> torch.sum(a)
tensor(-0.5475)
```

torch.sum(*input*, *dim*, *keepdim=False*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the sum of each row of the `input` tensor in the given
dimension `dim`. If `dim` is a list of dimensions,
reduce over all of them.

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

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Example:

```
>>> a = torch.randn(4, 4)
>>> a
tensor([[ 0.0569, -0.2475, 0.0737, -0.3429],
 [-0.2993, 0.9138, 0.9337, -1.6864],
 [ 0.1132, 0.7892, -0.1003, 0.5688],
 [ 0.3637, -0.9906, -0.4752, -1.5197]])
>>> torch.sum(a, 1)
tensor([-0.4598, -0.1381, 1.3708, -2.6217])
>>> b = torch.arange(4 * 5 * 6).view(4, 5, 6)
>>> torch.sum(b, (2, 1))
tensor([ 435., 1335., 2235., 3135.])
```