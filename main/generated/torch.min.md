# torch.min

torch.min(*input*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the minimum value of all elements in the `input` tensor.

Note

The difference between `max`/`min` and `amax`/`amin` is:

- `amax`/`amin` supports reducing on multiple dimensions,
- `amax`/`amin` does not return indices.

Both `amax`/`amin` evenly distribute gradients between equal values
when there are multiple input elements with the same minimum or maximum value.

For `max`/`min`:

- If reduce over all dimensions(no dim specified), gradients evenly distribute between equally `max`/`min` values.
- If reduce over one specified axis, only propagate to the indexed element.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randn(1, 3)
>>> a
tensor([[ 0.6750, 1.0857, 1.7197]])
>>> torch.min(a)
tensor(0.6750)
```

torch.min(*input*, *dim*, *keepdim=False*, ***, *out=None*)

Returns a namedtuple `(values, indices)` where `values` is the minimum
value of each row of the `input` tensor in the given dimension
`dim`. And `indices` is the index location of each minimum value found
(argmin).

If `keepdim` is `True`, the output tensors are of the same size as
`input` except in the dimension `dim` where they are of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in
the output tensors having 1 fewer dimension than `input`.

Note

If there are multiple minimal values in a reduced row then
the indices of the first minimal value are returned.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to reduce. If omitted, all dimensions are reduced. Explicit `None` is not supported.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**out** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*,**optional*) - the tuple of two output tensors (min, min_indices)

Example:

```
>>> a = torch.randn(4, 4)
>>> a
tensor([[-0.6248, 1.1334, -1.1899, -0.2803],
 [-1.4644, -0.2635, -0.3651, 0.6134],
 [ 0.2457, 0.0384, 1.0128, 0.7015],
 [-0.1153, 2.9849, 2.1458, 0.5788]])
>>> torch.min(a, 1)
torch.return_types.min(values=tensor([-1.1899, -1.4644, 0.0384, -0.1153]), indices=tensor([2, 0, 1, 0]))
```

torch.min(*input*, *other*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

See [`torch.minimum()`](torch.minimum.html#torch.minimum).