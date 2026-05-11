# torch.prod

torch.prod(*input: [Tensor](../tensors.html#torch.Tensor)*, ***, *dtype: _dtype | [None](https://docs.python.org/3/library/constants.html#None)*) → [Tensor](../tensors.html#torch.Tensor)

Returns the product of all elements in the `input` tensor.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.

Keyword Arguments:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Example:

```
>>> a = torch.randn(1, 3)
>>> a
tensor([[-0.8020, 0.5428, -1.5854]])
>>> torch.prod(a)
tensor(0.6902)
```

torch.prod(*input*, *dim*, *keepdim=False*, ***, *dtype=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the product of each row of the `input` tensor in the given
dimension `dim`.

If `keepdim` is `True`, the output tensor is of the same size
as `input` except in the dimension `dim` where it is of size 1.
Otherwise, `dim` is squeezed (see [`torch.squeeze()`](torch.squeeze.html#torch.squeeze)), resulting in
the output tensor having 1 fewer dimension than `input`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the dimension to reduce.
If `None`, all dimensions are reduced.
- **keepdim** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether the output tensor has `dim` retained or not. Default: `False`.

Keyword Arguments:

**dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.

Example:

```
>>> a = torch.randn(4, 2)
>>> a
tensor([[ 0.5261, -0.3837],
 [ 1.1857, -0.2498],
 [-1.1646, 0.0705],
 [ 1.1131, -1.0629]])
>>> torch.prod(a, 1)
tensor([-0.2018, -0.2962, -0.0821, -1.1831])
```