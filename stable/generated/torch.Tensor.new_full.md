# torch.Tensor.new_full

Tensor.new_full(*size*, *fill_value*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a Tensor of size [`size`](torch.Tensor.size.html#torch.Tensor.size) filled with `fill_value`.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Parameters:

**fill_value** (*scalar*) - the number to fill the output tensor with.

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
>>> tensor = torch.ones((2,), dtype=torch.float64)
>>> tensor.new_full((3, 4), 3.141592)
tensor([[ 3.1416, 3.1416, 3.1416, 3.1416],
 [ 3.1416, 3.1416, 3.1416, 3.1416],
 [ 3.1416, 3.1416, 3.1416, 3.1416]], dtype=torch.float64)
```