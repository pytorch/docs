# torch.fft.fftfreq

torch.fft.fftfreq(*n*, *d=1.0*, ***, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c8f2d26abd0de59995af555e80c82ca1221bc21b/torch/fft/__init__.py#L1231)

Computes the discrete Fourier Transform sample frequencies for a signal of size `n`.

Note

By convention, [`fft()`](torch.fft.fft.html#torch.fft.fft) returns positive frequency terms
first, followed by the negative frequencies in reverse order, so that
`f[-i]` for all 0<i≤n/2'0 < i \leq n/2`0<i≤n/2' in Python gives the negative
frequency terms. For an FFT of length `n` and with inputs spaced in
length unit `d`, the frequencies are:

```
f = [0, 1, ..., (n - 1) // 2, -(n // 2), ..., -1] / (d * n)
```

Note

For even lengths, the Nyquist frequency at `f[n/2]` can be thought of as
either negative or positive. `fftfreq()` follows NumPy's
convention of taking it to be negative.

Parameters:

- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the FFT length
- **d** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - The sampling length scale.
The spacing between individual samples of the FFT input.
The default assumes unit spacing, dividing that result by the actual
spacing gives the result in physical frequency units.

Keyword Arguments:

- **out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.
- **dtype** ([`torch.dtype`](../tensor_attributes.html#torch.dtype), optional) - the desired data type of returned tensor.
Default: if `None`, uses a global default (see [`torch.set_default_dtype()`](torch.set_default_dtype.html#torch.set_default_dtype)).
- **layout** ([`torch.layout`](../tensor_attributes.html#torch.layout), optional) - the desired layout of returned Tensor.
Default: `torch.strided`.
- **device** ([`torch.device`](../tensor_attributes.html#torch.device), optional) - the desired device of returned tensor.
Default: if `None`, uses the current device for the default tensor type
(see [`torch.set_default_device()`](torch.set_default_device.html#torch.set_default_device)). `device` will be the CPU
for CPU tensor types and the current CUDA device for CUDA tensor types.
- **requires_grad** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If autograd should record operations on the
returned tensor. Default: `False`.

Example

```
>>> torch.fft.fftfreq(5)
tensor([ 0.0000, 0.2000, 0.4000, -0.4000, -0.2000])
```

For even input, we can see the Nyquist frequency at `f[2]` is given as
negative:

```
>>> torch.fft.fftfreq(4)
tensor([ 0.0000, 0.2500, -0.5000, -0.2500])
```