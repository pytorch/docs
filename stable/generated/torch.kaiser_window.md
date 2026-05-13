# torch.kaiser_window

torch.kaiser_window(*window_length*, *periodic=True*, *beta=12.0*, ***, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)

Computes the Kaiser window with window length `window_length` and shape parameter `beta`.

Let I_0 be the zeroth order modified Bessel function of the first kind (see [`torch.i0()`](torch.i0.html#torch.i0)) and
`N = L - 1` if `periodic` is False and `L` if `periodic` is True,
where `L` is the `window_length`. This function computes:

outi=I0(β1−(i−N/2N/2)2)/I0(β)out_i = I_0 \left( \beta \sqrt{1 - \left( {\frac{i - N/2}{N/2}} \right) ^2 } \right) / I_0( \beta )

outi​=I0​​β1−(N/2i−N/2​)2​​/I0​(β)

Calling `torch.kaiser_window(L, B, periodic=True)` is equivalent to calling
`torch.kaiser_window(L + 1, B, periodic=False)[:-1])`.
The `periodic` argument is intended as a helpful shorthand
to produce a periodic window as input to functions like [`torch.stft()`](torch.stft.html#torch.stft).

Note

If `window_length` is one, then the returned window is a single element tensor containing a one.

Parameters:

- **window_length** ([*int*](https://docs.python.org/3/library/functions.html#int)) - length of the window.
- **periodic** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, returns a periodic window suitable for use in spectral analysis.
If False, returns a symmetric window suitable for use in filter design.
- **beta** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - shape parameter for the window.

Keyword Arguments:

- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)).
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned window tensor. Only
`torch.strided` (dense layout) is supported.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). [`device`](../tensor_attributes.html#torch.device) will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.