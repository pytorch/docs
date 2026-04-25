# torch.Tensor.new_tensor

Tensor.new_tensor(*data*, ***, *dtype=None*, *device=None*, *requires_grad=False*, *layout=torch.strided*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Returns a new Tensor with `data` as the tensor data.
By default, the returned Tensor has the same [`torch.dtype`](../tensor_attributes.html#torch.dtype) and
[`torch.device`](../tensor_attributes.html#torch.device) as this tensor.

Warning

`new_tensor()` always copies `data`. If you have a Tensor
`data` and want to avoid a copy, use [`torch.Tensor.requires_grad_()`](torch.Tensor.requires_grad_.html#torch.Tensor.requires_grad_)
or [`torch.Tensor.detach()`](torch.Tensor.detach.html#torch.Tensor.detach).
If you have a numpy array and want to avoid a copy, use
[`torch.from_numpy()`](torch.from_numpy.html#torch.from_numpy).

Warning

When data is a tensor x, `new_tensor()` reads out 'the data' from whatever it is passed,
and constructs a leaf variable. Therefore `tensor.new_tensor(x)` is equivalent to `x.detach().clone()`
and `tensor.new_tensor(x, requires_grad=True)` is equivalent to `x.detach().clone().requires_grad_(True)`.
The equivalents using `detach()` and `clone()` are recommended.

Parameters:

**data** (*array_like*) - The returned Tensor copies `data`.

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
>>> tensor = torch.ones((2,), dtype=torch.int8)
>>> data = [[0, 1], [2, 3]]
>>> tensor.new_tensor(data)
tensor([[ 0, 1],
 [ 2, 3]], dtype=torch.int8)
```