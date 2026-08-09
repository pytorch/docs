# torch.signal.windows.windows.nuttall

torch.signal.windows.windows.nuttall(*M*, ***, *sym=True*, *dtype=None*, *layout=torch.strided*, *device=None*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/signal/windows/windows.py#L822)

Computes the minimum 4-term Blackman-Harris window according to Nuttall.

wn=1−0.36358cos⁡(zn)+0.48917cos⁡(2zn)−0.13659cos⁡(3zn)+0.01064cos⁡(4zn)w_n = 1 - 0.36358 \cos{(z_n)} + 0.48917 \cos{(2z_n)} - 0.13659 \cos{(3z_n)} + 0.01064 \cos{(4z_n)}

wn​=1−0.36358cos(zn​)+0.48917cos(2zn​)−0.13659cos(3zn​)+0.01064cos(4zn​)

where zn=2πnMz_n = \frac{2 \pi n}{M}zn​=M2πn​.

The window is normalized to 1 (maximum value is 1). However, the 1 doesn't appear if `M` is even and `sym` is True.

Parameters:

**M** ([*int*](https://docs.python.org/3/library/functions.html#int)) - the length of the window.
In other words, the number of points of the returned window.

Keyword Arguments:

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

References:

```
- A. Nuttall, "Some windows with very good sidelobe behavior,"
 IEEE Transactions on Acoustics, Speech, and Signal Processing, vol. 29, no. 1, pp. 84-91,
 Feb 1981. https://doi.org/10.1109/TASSP.1981.1163506

- Heinzel G. et al., "Spectrum and spectral density estimation by the Discrete Fourier transform (DFT),
 including a comprehensive list of window functions and some new flat-top windows",
 February 15, 2002 https://holometer.fnal.gov/GH_FFT.pdf
```

Examples:

```
>>> # Generates a symmetric Nuttall window.
>>> torch.signal.windows.general_hamming(5, sym=True)
tensor([3.6280e-04, 2.2698e-01, 1.0000e+00, 2.2698e-01, 3.6280e-04])

>>> # Generates a periodic Nuttall window.
>>> torch.signal.windows.general_hamming(5, sym=False)
tensor([3.6280e-04, 1.1052e-01, 7.9826e-01, 7.9826e-01, 1.1052e-01])
```