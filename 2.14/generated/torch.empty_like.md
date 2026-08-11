# torch.empty_like

torch.empty_like(*input*, ***, *dtype=None*, *layout=None*, *device=None*, *requires_grad=False*, *memory_format=torch.preserve_format*) → [Tensor](../tensors.html#torch.Tensor)

Returns an uninitialized tensor with the same size as `input`.
`torch.empty_like(input)` is equivalent to
`torch.empty(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)`.

Note

If [`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms) and
[`torch.utils.deterministic.fill_uninitialized_memory`](../deterministic.html#torch.utils.deterministic.fill_uninitialized_memory) are both set to
`True`, the output tensor is initialized to prevent any possible
nondeterministic behavior from using the data as an input to an operation.
Floating point and complex tensors are filled with NaN, and integer tensors
are filled with the maximum value.

When `torch.preserve_format` is used:
If the input tensor is dense (i.e., non-overlapping strided),
its memory format (including strides) is retained.
Otherwise (e.g., a non-dense view like a stepped slice),
the output is converted to the dense format.

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
>>> a=torch.empty((2,3), dtype=torch.int32, device = 'cuda')
>>> torch.empty_like(a)
tensor([[0, 0, 0],
 [0, 0, 0]], device='cuda:0', dtype=torch.int32)
```