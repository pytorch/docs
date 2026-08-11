# torch.empty_permuted

torch.empty_permuted(*size*, *physical_layout*, ***, *dtype=None*, *layout=None*, *device=None*, *requires_grad=False*, *pin_memory=False*) → [Tensor](../tensors.html#torch.Tensor)

Creates an uninitialized, non-overlapping and dense tensor with the
specified `size`, with `physical_layout` specifying how the
dimensions are physically laid out in memory (each logical dimension is listed
from outermost to innermost). `physical_layout` is a generalization
of NCHW/NHWC notation: if each dimension is assigned a number according to
what order they occur in size (N=0, C=1, H=2, W=3), then NCHW is `(0, 1, 2, 3)`
while NHWC is `(0, 2, 3, 1)`. Equivalently, the strides of the output
tensor `t` are such that `t.stride(physical_layout[i]) == contiguous_strides[i]`
(notably, this function is *not* equivalent to `torch.empty(size).permute(physical_layout)`).

Unlike [`torch.empty_strided()`](torch.empty_strided.html#torch.empty_strided), this is guaranteed to produce a dense
tensor with no overlaps. If possible, prefer using this function over
[`torch.empty_strided()`](torch.empty_strided.html#torch.empty_strided) or manual use of [`torch.as_strided()`](torch.as_strided.html#torch.as_strided).

Note

If [`torch.use_deterministic_algorithms()`](torch.use_deterministic_algorithms.html#torch.use_deterministic_algorithms) and
[`torch.utils.deterministic.fill_uninitialized_memory`](../deterministic.html#torch.utils.deterministic.fill_uninitialized_memory) are both set to
`True`, the output tensor is initialized to prevent any possible
nondeterministic behavior from using the data as an input to an operation.
Floating point and complex tensors are filled with NaN, and integer tensors
are filled with the maximum value.

Parameters:

- **size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the shape of the output tensor
- **physical_layout** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*of*[*int*](https://docs.python.org/3/library/functions.html#int)) - the ordering of dimensions physically in memory

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

Examples

```
>>> torch.empty((2, 3, 5, 7)).stride()
(105, 35, 7, 1)
>>> torch.empty_permuted((2, 3, 5, 7), (0, 1, 2, 3)).stride()
(105, 35, 7, 1)
>>> torch.empty((2, 3, 5, 7), memory_format=torch.channels_last).stride()
(105, 1, 21, 3)
>>> torch.empty_permuted((2, 3, 5, 7), (0, 2, 3, 1)).stride()
(105, 1, 21, 3)
>>> torch.empty_permuted((2, 3, 5, 7), (0, 2, 3, 1)).dim_order()
(0, 2, 3, 1)
```