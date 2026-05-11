# torch.eye

torch.eye(*n*, *m=None*, ***, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a 2-D tensor with ones on the diagonal and zeros elsewhere.

Parameters:

- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the number of rows
- **m** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - the number of columns with default being `n`

Keyword Arguments:

- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)).
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Returns:

A 2-D tensor with ones on the diagonal and zeros elsewhere

Return type:

[Tensor](../tensors.html#torch.Tensor)

Example:

```
>>> torch.eye(3)
tensor([[ 1., 0., 0.],
 [ 0., 1., 0.],
 [ 0., 0., 1.]])
```