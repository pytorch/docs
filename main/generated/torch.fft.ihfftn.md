# torch.fft.ihfftn

torch.fft.ihfftn(*input*, *s=None*, *dim=None*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fft/__init__.py#L1161)

Computes the N-dimensional inverse discrete Fourier transform of real `input`.

`input` must be a real-valued signal, interpreted in the Fourier domain.
The n-dimensional IFFT of a real signal is Hermitian-symmetric,
`X[i, j, ...] = conj(X[-i, -j, ...])`. `ihfftn()` represents
this in the one-sided form where only the positive frequencies below the
Nyquist frequency are included in the last signal dimension. To compute the
full output, use [`ifftn()`](torch.fft.ifftn.html#torch.fft.ifftn).

Note

Supports torch.half on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimensions.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **s** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Signal size in the transformed dimensions.
If given, each dimension `dim[i]` will either be zero-padded or
trimmed to the length `s[i]` before computing the Hermitian IFFT.
If a length `-1` is specified, no padding is done in that dimension.
Default: `s = [input.size(d) for d in dim]`
- **dim** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Dimensions to be transformed.
Default: all dimensions, or the last `len(s)` dimensions if `s` is given.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the backward transform
(`ihfftn()`), these correspond to:

- `"forward"` - no normalization
- `"backward"` - normalize by `1/n`
- `"ortho"` - normalize by `1/sqrt(n)` (making the Hermitian IFFT orthonormal)

Where `n = prod(s)` is the logical IFFT size.
Calling the forward transform ([`hfftn()`](torch.fft.hfftn.html#torch.fft.hfftn)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make `ihfftn()`
the exact inverse.

Default is `"backward"` (normalize by `1/n`).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> T = torch.rand(10, 10)
>>> ihfftn = torch.fft.ihfftn(T)
>>> ihfftn.size()
torch.Size([10, 6])
```

Compared against the full output from [`ifftn()`](torch.fft.ifftn.html#torch.fft.ifftn), we have all
elements up to the Nyquist frequency.

```
>>> ifftn = torch.fft.ifftn(t)
>>> torch.allclose(ifftn[..., :6], ihfftn)
True
```

The discrete Fourier transform is separable, so `ihfftn()`
here is equivalent to a combination of [`ihfft()`](torch.fft.ihfft.html#torch.fft.ihfft) and
[`ifft()`](torch.fft.ifft.html#torch.fft.ifft):

```
>>> two_iffts = torch.fft.ifft(torch.fft.ihfft(t, dim=1), dim=0)
>>> torch.allclose(ihfftn, two_iffts)
True
```