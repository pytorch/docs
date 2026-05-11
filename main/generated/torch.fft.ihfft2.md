# torch.fft.ihfft2

torch.fft.ihfft2(*input*, *s=None*, *dim=(-2, -1)*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fft/__init__.py#L1003)

Computes the 2-dimensional inverse discrete Fourier transform of real
`input`. Equivalent to [`ihfftn()`](torch.fft.ihfftn.html#torch.fft.ihfftn) but transforms only the
two last dimensions by default.

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
Default: last two dimensions.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the backward transform
(`ihfft2()`), these correspond to:

- `"forward"` - no normalization
- `"backward"` - normalize by `1/n`
- `"ortho"` - normalize by `1/sqrt(n)` (making the Hermitian IFFT orthonormal)

Where `n = prod(s)` is the logical IFFT size.
Calling the forward transform ([`hfft2()`](torch.fft.hfft2.html#torch.fft.hfft2)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make `ihfft2()`
the exact inverse.

Default is `"backward"` (normalize by `1/n`).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> T = torch.rand(10, 10)
>>> t = torch.fft.ihfft2(t)
>>> t.size()
torch.Size([10, 6])
```

Compared against the full output from [`ifft2()`](torch.fft.ifft2.html#torch.fft.ifft2), the
Hermitian time-space signal takes up only half the space.

```
>>> fftn = torch.fft.ifft2(t)
>>> torch.allclose(fftn[..., :6], rfftn)
True
```

The discrete Fourier transform is separable, so `ihfft2()`
here is equivalent to a combination of [`ifft()`](torch.fft.ifft.html#torch.fft.ifft) and
[`ihfft()`](torch.fft.ihfft.html#torch.fft.ihfft):

```
>>> two_ffts = torch.fft.ifft(torch.fft.ihfft(t, dim=1), dim=0)
>>> torch.allclose(t, two_ffts)
True
```