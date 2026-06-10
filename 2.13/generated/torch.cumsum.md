# torch.cumsum

torch.cumsum(*input*, *dim*, ***, *dtype=None*, *out=None*) → [Tensor](../tensors.html#torch.Tensor)

Returns the cumulative sum of elements of `input` in the dimension
`dim`.

For example, if `input` is a vector of size N, the result will also be
a vector of size N, with elements.

yi=x1+x2+x3+⋯+xiy_i = x_1 + x_2 + x_3 + \dots + x_i

yi​=x1​+x2​+x3​+⋯+xi​
Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the dimension to do the operation over

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
If specified, the input tensor is casted to [`dtype`](../tensor_attributes.html#torch.dtype) before the operation
is performed. This is useful for preventing data type overflows. Default: None.
- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example:

```
>>> a = torch.randint(1, 20, (10,))
>>> a
tensor([13, 7, 3, 10, 13, 3, 15, 10, 9, 10])
>>> torch.cumsum(a, dim=0)
tensor([13, 20, 23, 33, 46, 49, 64, 74, 83, 93])
```