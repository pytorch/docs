# torch.fft.ifftshift

torch.fft.ifftshift(*input*, *dim=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/e7003ce301964b7a4ef5d2d4777331489745a93c/torch/fft/__init__.py#L1414)

Inverse of [`fftshift()`](torch.fft.fftshift.html#torch.fft.fftshift).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the tensor in FFT order
- **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)*,**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]**,**optional*) - The dimensions to rearrange.
Only dimensions specified here will be rearranged, any other dimensions
will be left in their original order.
Default: All dimensions of `input`.

Example

```
>>> f = torch.fft.fftfreq(5)
>>> f
tensor([ 0.0000, 0.2000, 0.4000, -0.4000, -0.2000])
```

A round-trip through [`fftshift()`](torch.fft.fftshift.html#torch.fft.fftshift) and
`ifftshift()` gives the same result:

```
>>> shifted = torch.fft.fftshift(f)
>>> torch.fft.ifftshift(shifted)
tensor([ 0.0000, 0.2000, 0.4000, -0.4000, -0.2000])
```