# torch.fft.ifft

torch.fft.ifft(*input*, *n=None*, *dim=-1*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/f7811aa3c052ace6751fbc2f6bc93908b9ea6b9f/torch/fft/__init__.py#L88)

Computes the one dimensional inverse discrete Fourier transform of `input`.

Note

Supports torch.half and torch.chalf on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimension.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **n** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - Signal length. If given, the input will either be zero-padded
or trimmed to this length before computing the IFFT.
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**optional*) - The dimension along which to take the one dimensional IFFT.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the backward transform
(`ifft()`), these correspond to:

- `"forward"` - no normalization
- `"backward"` - normalize by `1/n`
- `"ortho"` - normalize by `1/sqrt(n)` (making the IFFT orthonormal)

Calling the forward transform ([`fft()`](torch.fft.fft.html#torch.fft.fft)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make `ifft()`
the exact inverse.

Default is `"backward"` (normalize by `1/n`).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> t = torch.tensor([ 6.+0.j, -2.+2.j, -2.+0.j, -2.-2.j])
>>> torch.fft.ifft(t)
tensor([0.+0.j, 1.+0.j, 2.+0.j, 3.+0.j])
```