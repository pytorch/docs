# torch.signal.windows.windows.exponential

torch.signal.windows.windows.exponential(*M*, ***, *center=None*, *tau=1.0*, *sym=True*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/signal/windows/windows.py#L89)

Computes a window with an exponential waveform.
Also known as Poisson window.

The exponential window is defined as follows:

wn=exp⁡(−∣n−c∣τ)w_n = \exp{\left(-\frac{|n - c|}{\tau}\right)}

wn​=exp(−τ∣n−c∣​)

where c is the `center` of the window.

The window is normalized to 1 (maximum value is 1). However, the 1 doesn't appear if `M` is even and `sym` is True.

Parameters:

**M** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the length of the window.
In other words, the number of points of the returned window.

Keyword Arguments:

- **center** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - where the center of the window will be located.
Default: M / 2 if sym is False, else (M - 1) / 2.
- **tau** ([*float*](https://docs.python.org/3/library/functions.html#float)*,**optional*) - the decay value.
Tau is generally associated with a percentage, that means, that the value should
vary within the interval (0, 100]. If tau is 100, it is considered the uniform window.
Default: 1.0.
- **sym** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If False, returns a periodic window suitable for use in spectral analysis.
If True, returns a symmetric window suitable for use in filter design. Default: True.
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

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Examples:

```
>>> # Generates a symmetric exponential window of size 10 and with a decay value of 1.0.
>>> # The center will be at (M - 1) / 2, where M is 10.
>>> torch.signal.windows.exponential(10)
tensor([0.0111, 0.0302, 0.0821, 0.2231, 0.6065, 0.6065, 0.2231, 0.0821, 0.0302, 0.0111])

>>> # Generates a periodic exponential window and decay factor equal to .5
>>> torch.signal.windows.exponential(10, sym=False,tau=.5)
tensor([4.5400e-05, 3.3546e-04, 2.4788e-03, 1.8316e-02, 1.3534e-01, 1.0000e+00, 1.3534e-01, 1.8316e-02, 2.4788e-03, 3.3546e-04])
```