# torch.fft.ifftn

torch.fft.ifftn(*input*, *s=None*, *dim=None*, *norm=None*, ***, *out=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/fft/__init__.py#L303)

Computes the N dimensional inverse discrete Fourier transform of `input`.

Note

Supports torch.half and torch.chalf on CUDA with GPU Architecture SM53 or greater.
However it only supports powers of 2 signal length in every transformed dimensions.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **s** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Signal size in the transformed dimensions.
If given, each dimension `dim[i]` will either be zero-padded or
trimmed to the length `s[i]` before computing the IFFT.
If a length `-1` is specified, no padding is done in that dimension.
Default: `s = [input.size(d) for d in dim]`
- **dim** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - Dimensions to be transformed.
Default: all dimensions, or the last `len(s)` dimensions if `s` is given.
- **norm** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) -

Normalization mode. For the backward transform
(`ifftn()`), these correspond to:

- `"forward"` - no normalization
- `"backward"` - normalize by `1/n`
- `"ortho"` - normalize by `1/sqrt(n)` (making the IFFT orthonormal)

Where `n = prod(s)` is the logical IFFT size.
Calling the forward transform ([`fftn()`](torch.fft.fftn.html#torch.fft.fftn)) with the same
normalization mode will apply an overall normalization of `1/n` between
the two transforms. This is required to make `ifftn()`
the exact inverse.

Default is `"backward"` (normalize by `1/n`).

Keyword Arguments:

**out** ([*Tensor*](../tensors.html#torch.Tensor)*,**optional*) - the output tensor.

Example

```
>>> x = torch.rand(10, 10, dtype=torch.complex64)
>>> ifftn = torch.fft.ifftn(x)
```

The discrete Fourier transform is separable, so `ifftn()`
here is equivalent to two one-dimensional [`ifft()`](torch.fft.ifft.html#torch.fft.ifft) calls:

```
>>> two_iffts = torch.fft.ifft(torch.fft.ifft(x, dim=0), dim=1)
>>> torch.testing.assert_close(ifftn, two_iffts, check_stride=False)
```