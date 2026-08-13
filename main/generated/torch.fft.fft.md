# torch.fft.fft

torch.fft.fft(*input*, *n=None*, *dim=-1*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fft/__init__.py#L33)

Computes the one dimensional discrete Fourier transform of `input`.

Note

The Fourier domain representation of any real signal satisfies the
Hermitian property: X[i] = conj(X[-i]). This function always returns both
the positive and negative frequency terms even though, for real inputs, the
negative frequencies are redundant. [`rfft()`](torch.fft.rfft.html#torch.fft.rfft) returns the
more compact one-sided representation where only the positive frequencies
are returned.

Note

Supports torch.half and torch.chalf on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimension.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Signal length. If given, the input will either be zero-padded
or trimmed to this length before computing the FFT.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The dimension along which to take the one dimensional FFT.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the forward transform
(`fft()`), these correspond to:

- `"forward"` - normalize by `1/n`
- `"backward"` - no normalization
- `"ortho"` - normalize by `1/sqrt(n)` (making the FFT orthonormal)

Calling the backward transform ([`ifft()`](torch.fft.ifft.html#torch.fft.ifft)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make [`ifft()`](torch.fft.ifft.html#torch.fft.ifft)
the exact inverse.

Default is `"backward"` (no normalization).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> t = torch.arange(4)
>>> t
tensor([0, 1, 2, 3])
>>> torch.fft.fft(t)
tensor([ 6.+0.j, -2.+2.j, -2.+0.j, -2.-2.j])
```

```
>>> t = torch.tensor([0.+1.j, 2.+3.j, 4.+5.j, 6.+7.j])
>>> torch.fft.fft(t)
tensor([12.+16.j, -8.+0.j, -4.-4.j, 0.-8.j])
```