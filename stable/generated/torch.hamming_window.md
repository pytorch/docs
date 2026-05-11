# torch.hamming_window

torch.hamming_window(*window_length*, ***, *dtype=None*, *layout=None*, *device=None*, *pin_memory=False*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Hamming window function.

w[n]=α−β cos⁡(2πnN−1),w[n] = \alpha - \beta\ \cos \left( \frac{2 \pi n}{N - 1} \right),

w[n]=α−β cos(N−12πn​),

where NNN is the full window size.

The input `window_length` is a positive integer controlling the
returned window size. `periodic` flag determines whether the returned
window trims off the last duplicate value from the symmetric window and is
ready to be used as a periodic window with functions like
[`torch.stft()`](torch.stft.html#torch.stft). Therefore, if `periodic` is true, the NNN in
above formula is in fact window_length+1\text{window\_length} + 1window_length+1. Also, we always have
`torch.hamming_window(L, periodic=True)` equal to
`torch.hamming_window(L + 1, periodic=False)[:-1])`.

Note

If `window_length` =1=1=1, the returned window contains a single value 1.

Note

This is a generalized version of [`torch.hann_window()`](torch.hann_window.html#torch.hann_window).

Parameters:

**window_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of returned window

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)). Only floating point types are supported.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned window tensor. Only
`torch.strided` (dense layout) is supported.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Returns:

A 1-D tensor of size (window_length,)(\text{window\_length},)(window_length,) containing the window.

Return type:

[Tensor](../tensors.html#torch.Tensor)

torch.hamming_window(*window_length*, *periodic*, ***, *dtype=None*, *layout=None*, *device=None*, *pin_memory=False*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Hamming window function with periodic specified.

Parameters:

- **window_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of returned window
- **periodic** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, returns a window to be used as periodic
function. If False, return a symmetric window.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)). Only floating point types are supported.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned window tensor. Only
`torch.strided` (dense layout) is supported.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Returns:

A 1-D tensor of size (window_length,)(\text{window\_length},)(window_length,) containing the window.

Return type:

[Tensor](../tensors.html#torch.Tensor)

torch.hamming_window(*window_length*, *periodic*, *float alpha*, ***, *dtype=None*, *layout=None*, *device=None*, *pin_memory=False*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Hamming window function with periodic and alpha specified.

Parameters:

- **window_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of returned window
- **periodic** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, returns a window to be used as periodic
function. If False, return a symmetric window.
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The coefficient α\alphaα in the equation above

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)). Only floating point types are supported.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned window tensor. Only
`torch.strided` (dense layout) is supported.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Returns:

A 1-D tensor of size (window_length,)(\text{window\_length},)(window_length,) containing the window.

Return type:

[Tensor](../tensors.html#torch.Tensor)

torch.hamming_window(*window_length*, *periodic*, *float alpha*, *float beta*, ***, *dtype=None*, *layout=None*, *device=None*, *pin_memory=False*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Hamming window function with periodic, alpha and beta specified.

Parameters:

- **window_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of returned window
- **periodic** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - If True, returns a window to be used as periodic
function. If False, return a symmetric window.
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The coefficient α\alphaα in the equation above
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The coefficient β\betaβ in the equation above

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)). Only floating point types are supported.
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned window tensor. Only
`torch.strided` (dense layout) is supported.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **pin_memory** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If set, returned tensor would be allocated in
the pinned memory. Works only for CPU tensors. Default: `False`.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Returns:

A 1-D tensor of size (window_length,)(\text{window\_length},)(window_length,) containing the window.

Return type:

[Tensor](../tensors.html#torch.Tensor)