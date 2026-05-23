# torch.fft.fft2

torch.fft.fft2(*input*, *s=None*, *dim=(-2, -1)*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/2f696474dc8fe614670ddb889f4ae1c75d1a11e6/torch/fft/__init__.py#L129)

Computes the 2 dimensional discrete Fourier transform of `input`.
Equivalent to [`fftn()`](torch.fft.fftn.html#torch.fft.fftn) but FFTs only the last two dimensions by default.

Note

The Fourier domain representation of any real signal satisfies the
Hermitian property: `X[i, j] = conj(X[-i, -j])`. This
function always returns all positive and negative frequency terms even
though, for real inputs, half of these values are redundant.
[`rfft2()`](torch.fft.rfft2.html#torch.fft.rfft2) returns the more compact one-sided representation
where only the positive frequencies of the last dimension are returned.

Note

Supports torch.half and torch.chalf on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimensions.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **s** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Signal size in the transformed dimensions.
If given, each dimension `dim[i]` will either be zero-padded or
trimmed to the length `s[i]` before computing the FFT.
If a length `-1` is specified, no padding is done in that dimension.
Default: `s = [input.size(d) for d in dim]`
- **dim** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Dimensions to be transformed.
Default: last two dimensions.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the forward transform
(`fft2()`), these correspond to:

- `"forward"` - normalize by `1/n`
- `"backward"` - no normalization
- `"ortho"` - normalize by `1/sqrt(n)` (making the FFT orthonormal)

Where `n = prod(s)` is the logical FFT size.
Calling the backward transform ([`ifft2()`](torch.fft.ifft2.html#torch.fft.ifft2)) with the same
normalization mode will apply an overall normalization of `1/n`
between the two transforms. This is required to make
[`ifft2()`](torch.fft.ifft2.html#torch.fft.ifft2) the exact inverse.

Default is `"backward"` (no normalization).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> x = torch.rand(10, 10, dtype=torch.complex64)
>>> fft2 = torch.fft.fft2(x)
```

The discrete Fourier transform is separable, so `fft2()`
here is equivalent to two one-dimensional [`fft()`](torch.fft.fft.html#torch.fft.fft) calls:

```
>>> two_ffts = torch.fft.fft(torch.fft.fft(x, dim=0), dim=1)
>>> torch.testing.assert_close(fft2, two_ffts, check_stride=False)
```