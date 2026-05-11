# torch.empty_strided

torch.empty_strided(*size*, *stride*, ***, *dtype=None*, *layout=None*, *device=None*, *requires_grad=False*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Creates a tensor with the specified `size` and `stride` and filled with undefined data.

Warning

If the constructed tensor is "overlapped" (with multiple indices referring to the same element
in memory) its behavior is undefined.

Note

If [`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms) and
[`torch.utils.deterministic.fill_uninitialized_memory`](../deterministic.html#torch.utils.deterministic.fill_uninitialized_memory) are both set to
`True`, the output tensor is initialized to prevent any possible
nondeterministic behavior from using the data as an input to an operation.
Floating point and complex tensors are filled with NaN, and integer tensors
are filled with the maximum value.

Parameters:

- **size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the shape of the output tensor
- **stride** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the strides of the output tensor

Keyword Arguments:

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
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.

Example:

```
>>> a = torch.empty_strided((2, 3), (1, 2))
>>> a
tensor([[8.9683e-44, 4.4842e-44, 5.1239e+07],
 [0.0000e+00, 0.0000e+00, 3.0705e-41]])
>>> a.stride()
(1, 2)
>>> a.size()
torch.Size([2, 3])
```