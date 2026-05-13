# torch.full_like

torch.full_like(*input*, *fill_value*, *\**, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor with the same size as `input` filled with `fill_value`.
`torch.full_like(input, fill_value)` is equivalent to
`torch.full(input.size(), fill_value, dtype=input.dtype, layout=input.layout, device=input.device)`.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the size of `input` will determine size of the output tensor.
- **fill_value** - the number to fill the output tensor with.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned Tensor.
Default: if `None`, defaults to the dtype of `input`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned tensor.
Default: if `None`, defaults to the layout of `input`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, defaults to the device of `input`.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **memory_format** ([`torch.memory_format`](../tensor_attributes.html#torch.memory_format), optional) - the desired memory format of
returned Tensor. Default: `torch.preserve_format`.

Example:

```
>>> x = torch.ones(2, 3)
>>> torch.full_like(x, 3.141592)
tensor([[ 3.1416, 3.1416, 3.1416],
 [ 3.1416, 3.1416, 3.1416]])
>>> torch.full_like(x, 7)
tensor([[7., 7., 7.],
 [7., 7., 7.]])
>>> torch.full_like(x, 0.5, dtype=torch.int32)
tensor([[0, 0, 0],
 [0, 0, 0]], dtype=torch.int32)
>>> y = torch.randn(3, 4, dtype=torch.float64)
>>> torch.full_like(y, -1.0)
tensor([[-1., -1., -1., -1.],
 [-1., -1., -1., -1.],
 [-1., -1., -1., -1.]], dtype=torch.float64)
```