# torch.fft.ihfft

torch.fft.ihfft(*input*, *n=None*, *dim=-1*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/fft/__init__.py#L876)

Computes the inverse of [`hfft()`](torch.fft.hfft.html#torch.fft.hfft).

`input` must be a real-valued signal, interpreted in the Fourier domain.
The IFFT of a real signal is Hermitian-symmetric, `X[i] = conj(X[-i])`.
`ihfft()` represents this in the one-sided form where only the
positive frequencies below the Nyquist frequency are included. To compute the
full output, use [`ifft()`](torch.fft.ifft.html#torch.fft.ifft).

Note

Supports torch.half on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimension.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the real input tensor
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Signal length. If given, the input will either be zero-padded
or trimmed to this length before computing the Hermitian IFFT.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The dimension along which to take the one dimensional Hermitian IFFT.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the backward transform
(`ihfft()`), these correspond to:

- `"forward"` - no normalization
- `"backward"` - normalize by `1/n`
- `"ortho"` - normalize by `1/sqrt(n)` (making the IFFT orthonormal)

Calling the forward transform ([`hfft()`](torch.fft.hfft.html#torch.fft.hfft)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make `ihfft()`
the exact inverse.

Default is `"backward"` (normalize by `1/n`).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> t = torch.arange(5)
>>> t
tensor([0, 1, 2, 3, 4])
>>> torch.fft.ihfft(t)
tensor([ 2.0000-0.0000j, -0.5000-0.6882j, -0.5000-0.1625j])
```

Compare against the full output from [`ifft()`](torch.fft.ifft.html#torch.fft.ifft):

```
>>> torch.fft.ifft(t)
tensor([ 2.0000-0.0000j, -0.5000-0.6882j, -0.5000-0.1625j, -0.5000+0.1625j,
 -0.5000+0.6882j])
```