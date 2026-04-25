# torch.blackman_window

torch.blackman_window(*window_length*, *periodic=True*, ***, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Blackman window function.

w[n]=0.42−0.5cos⁡(2πnN−1)+0.08cos⁡(4πnN−1)w[n] = 0.42 - 0.5 \cos \left( \frac{2 \pi n}{N - 1} \right) + 0.08 \cos \left( \frac{4 \pi n}{N - 1} \right)

w[n]=0.42−0.5cos(N−12πn​)+0.08cos(N−14πn​)

where NNN is the full window size.

The input `window_length` is a positive integer controlling the
returned window size. `periodic` flag determines whether the returned
window trims off the last duplicate value from the symmetric window and is
ready to be used as a periodic window with functions like
[`torch.stft()`](torch.stft.html#torch.stft). Therefore, if `periodic` is true, the NNN in
above formula is in fact window_length+1\text{window\_length} + 1window_length+1. Also, we always have
`torch.blackman_window(L, periodic=True)` equal to
`torch.blackman_window(L + 1, periodic=False)[:-1]`.

Note

If `window_length` =1=1=1, the returned window contains a single value 1.

Parameters:

- **window_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the size of returned window
- **periodic** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, returns a window to be used as periodic
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
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Returns:

A 1-D tensor of size (window_length,)(\text{window\_length},)(window_length,) containing the window

Return type:

[Tensor](../tensors.html#torch.Tensor)