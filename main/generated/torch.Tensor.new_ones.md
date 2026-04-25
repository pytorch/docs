# torch.Tensor.new_ones

Tensor.new_ones(*size*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size [`size`](torch.Tensor.size.html#torch.Tensor.size) filled with `1`.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**size** ([*int*](https://docs.python.org/3/library/functions.html#int)*...*) - a list, tuple, or [`torch.Size`](../size.html#torch.Size) of integers defining the
shape of the output tensor.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired type of returned tensor.
Default: if None, same [`torch.dtype`](../tensor_attributes.html#torch.dtype) as this tensor.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if None, same [`torch.device`](../tensor_attributes.html#torch.device) as this tensor.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> tensor = torch.tensor((), dtype=torch.int32)
>>> tensor.new_ones((2, 3))
tensor([[ 1, 1, 1],
 [ 1, 1, 1]], dtype=torch.int32)
```