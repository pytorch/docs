# upsample

*class*torch.ao.nn.quantized.functional.upsample(*input*, *size=None*, *scale_factor=None*, *mode='nearest'*, *align_corners=None*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/ao/nn/quantized/functional.py#L676)

Upsamples the input to either the given `size` or the given
`scale_factor`

Warning

This function is deprecated in favor of
[`torch.ao.nn.quantized.functional.interpolate()`](torch.ao.nn.quantized.functional.interpolate.html#torch.ao.nn.quantized.functional.interpolate).
This is equivalent with `nn.quantized.functional.interpolate(...)`.

See [`torch.nn.functional.interpolate()`](torch.nn.functional.interpolate.html#torch.nn.functional.interpolate) for implementation details.

The input dimensions are interpreted in the form:
mini-batch x channels x [optional depth] x [optional height] x width.

Note

The input quantization parameters propagate to the output.

Note

Only 2D input is supported for quantized inputs

Note

Only the following modes are supported for the quantized inputs:

- bilinear
- nearest

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input tensor
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial size.
- **scale_factor** ([*float*](https://docs.python.org/3/library/functions.html#float)*or**Tuple**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - multiplier for spatial size. Has to be an integer.
- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - algorithm used for upsampling:
`'nearest'` | `'bilinear'`
- **align_corners** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Geometrically, we consider the pixels of the
input and output as squares rather than points.
If set to `True`, the input and output tensors are aligned by the
center points of their corner pixels, preserving the values at the corner pixels.
If set to `False`, the input and output tensors are aligned by the corner
points of their corner pixels, and the interpolation uses edge value padding
for out-of-boundary values, making this operation *independent* of input size
when `scale_factor` is kept the same. This only has an effect when `mode`
is `'bilinear'`.
Default: `False`

Warning

With `align_corners = True`, the linearly interpolating modes
(bilinear) don't proportionally align the
output and input pixels, and thus the output values can depend on the
input size. This was the default behavior for these modes up to version
0.3.1. Since then, the default behavior is `align_corners = False`.
See [`Upsample`](torch.nn.Upsample.html#torch.nn.Upsample) for concrete examples on how this
affects the outputs.