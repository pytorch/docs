# torch.zeros_like

torch.zeros_like(*input*, ***, *dtype=None*, *layout=None*, *device=None*, *requires_grad=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns a tensor filled with the scalar value 0, with the same size as
`input`. `torch.zeros_like(input)` is equivalent to
`torch.zeros(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)`.

Warning

As of 0.4, this function does not support an `out` keyword. As an alternative,
the old `torch.zeros_like(input, out=output)` is equivalent to
`torch.zeros(input.size(), out=output)`.

Parameters:

**input** ([*Tensor*](../tensors.html#torch.Tensor)) - the size of `input` will determine size of the output tensor.

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
>>> input = torch.empty(2, 3)
>>> torch.zeros_like(input)
tensor([[ 0., 0., 0.],
 [ 0., 0., 0.]])
```