# torch.fft.fftn

torch.fft.fftn(*input*, *s=None*, *dim=None*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/fft/__init__.py#L243)

Computes the N dimensional discrete Fourier transform of `input`.

Note

The Fourier domain representation of any real signal satisfies the
Hermitian property: `X[i_1, ..., i_n] = conj(X[-i_1, ..., -i_n])`. This
function always returns all positive and negative frequency terms even
though, for real inputs, half of these values are redundant.
[`rfftn()`](torch.fft.rfftn.html#torch.fft.rfftn) returns the more compact one-sided representation
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
Default: all dimensions, or the last `len(s)` dimensions if `s` is given.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the forward transform
(`fftn()`), these correspond to:

- `"forward"` - normalize by `1/n`
- `"backward"` - no normalization
- `"ortho"` - normalize by `1/sqrt(n)` (making the FFT orthonormal)

Where `n = prod(s)` is the logical FFT size.
Calling the backward transform ([`ifftn()`](torch.fft.ifftn.html#torch.fft.ifftn)) with the same
normalization mode will apply an overall normalization of `1/n`
between the two transforms. This is required to make
[`ifftn()`](torch.fft.ifftn.html#torch.fft.ifftn) the exact inverse.

Default is `"backward"` (no normalization).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> x = torch.rand(10, 10, dtype=torch.complex64)
>>> fftn = torch.fft.fftn(x)
```

The discrete Fourier transform is separable, so `fftn()`
here is equivalent to two one-dimensional [`fft()`](torch.fft.fft.html#torch.fft.fft) calls:

```
>>> two_ffts = torch.fft.fft(torch.fft.fft(x, dim=0), dim=1)
>>> torch.testing.assert_close(fftn, two_ffts, check_stride=False)
```