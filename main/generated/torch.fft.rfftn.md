# torch.fft.rfftn

torch.fft.rfftn(*input*, *s=None*, *dim=None*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/fft/__init__.py#L637)

Computes the N-dimensional discrete Fourier transform of real `input`.

The FFT of a real signal is Hermitian-symmetric,
`X[i_1, ..., i_n] = conj(X[-i_1, ..., -i_n])` so the full
[`fftn()`](torch.fft.fftn.html#torch.fft.fftn) output contains redundant information.
`rfftn()` instead omits the negative frequencies in the
last dimension.

Note

Supports torch.half on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimensions.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **s** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Signal size in the transformed dimensions.
If given, each dimension `dim[i]` will either be zero-padded or
trimmed to the length `s[i]` before computing the real FFT.
If a length `-1` is specified, no padding is done in that dimension.
Default: `s = [input.size(d) for d in dim]`
- **dim** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Dimensions to be transformed.
Default: all dimensions, or the last `len(s)` dimensions if `s` is given.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the forward transform
(`rfftn()`), these correspond to:

- `"forward"` - normalize by `1/n`
- `"backward"` - no normalization
- `"ortho"` - normalize by `1/sqrt(n)` (making the real FFT orthonormal)

Where `n = prod(s)` is the logical FFT size.
Calling the backward transform ([`irfftn()`](torch.fft.irfftn.html#torch.fft.irfftn)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make [`irfftn()`](torch.fft.irfftn.html#torch.fft.irfftn)
the exact inverse.

Default is `"backward"` (no normalization).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> t = torch.rand(10, 10)
>>> rfftn = torch.fft.rfftn(t)
>>> rfftn.size()
torch.Size([10, 6])
```

Compared against the full output from [`fftn()`](torch.fft.fftn.html#torch.fft.fftn), we have all
elements up to the Nyquist frequency.

```
>>> fftn = torch.fft.fftn(t)
>>> torch.testing.assert_close(fftn[..., :6], rfftn, check_stride=False)
```

The discrete Fourier transform is separable, so `rfftn()`
here is equivalent to a combination of [`fft()`](torch.fft.fft.html#torch.fft.fft) and
[`rfft()`](torch.fft.rfft.html#torch.fft.rfft):

```
>>> two_ffts = torch.fft.fft(torch.fft.rfft(t, dim=1), dim=0)
>>> torch.testing.assert_close(rfftn, two_ffts, check_stride=False)
```