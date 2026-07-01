# torch.fft.rfftfreq

torch.fft.rfftfreq(*n*, *d=1.0*, ***, *out=None*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/df6ed392bccc6625dbf4f6a82bcecee03433aa18/torch/fft/__init__.py#L1280)

Computes the sample frequencies for [`rfft()`](torch.fft.rfft.html#torch.fft.rfft) with a signal of size `n`.

Note

[`rfft()`](torch.fft.rfft.html#torch.fft.rfft) returns Hermitian one-sided output, so only the
positive frequency terms are returned. For a real FFT of length `n`
and with inputs spaced in length unit `d`, the frequencies are:

```
f = torch.arange((n + 1) // 2) / (d * n)
```

Note

For even lengths, the Nyquist frequency at `f[n/2]` can be thought of as
either negative or positive. Unlike [`fftfreq()`](torch.fft.fftfreq.html#torch.fft.fftfreq),
`rfftfreq()` always returns it as positive.

Parameters:

- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the real FFT length
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
>>> torch.fft.rfftfreq(5)
tensor([0.0000, 0.2000, 0.4000])
```

```
>>> torch.fft.rfftfreq(4)
tensor([0.0000, 0.2500, 0.5000])
```

Compared to the output from [`fftfreq()`](torch.fft.fftfreq.html#torch.fft.fftfreq), we see that the
Nyquist frequency at `f[2]` has changed sign:
>>> torch.fft.fftfreq(4)
tensor([ 0.0000, 0.2500, -0.5000, -0.2500])