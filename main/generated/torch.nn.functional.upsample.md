# torch.nn.functional.upsample

torch.nn.functional.upsample(*input*, *size=None*, *scale_factor=None*, *mode='nearest'*, *align_corners=None*)[[source]](https://github.com/pytorch/pytorch/blob/dff44973f3eba04a92de8499c17cd237997140f2/torch/nn/functional.py#L4478)

Upsample input.

Provided tensor is upsampled to either the given `size` or the given
`scale_factor`

Warning

This function is deprecated in favor of [`torch.nn.functional.interpolate()`](torch.nn.functional.interpolate.html#torch.nn.functional.interpolate).
This is equivalent with `nn.functional.interpolate(...)`.

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.

The algorithm used for upsampling is determined by `mode`.

Currently temporal, spatial and volumetric upsampling are supported, i.e.
expected inputs are 3-D, 4-D or 5-D in shape.

The input dimensions are interpreted in the form:
mini-batch x channels x [optional depth] x [optional height] x width.

The modes available for upsampling are: nearest, linear (3D-only),
bilinear, bicubic (4D-only), trilinear (5D-only), lanczos (4D-only)

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial size.
- **scale_factor** ([*float*](https://docs.python.org/3/library/functions.html#float)*or**Tuple**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - multiplier for spatial size. Has to match input size if it is a tuple.
- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - algorithm used for upsampling:
`'nearest'` | `'linear'` | `'bilinear'` | `'bicubic'` |
`'trilinear'` | `'lanczos'`. Default: `'nearest'`
- **align_corners** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Geometrically, we consider the pixels of the
input and output as squares rather than points.
If set to `True`, the input and output tensors are aligned by the
center points of their corner pixels, preserving the values at the corner pixels.
If set to `False`, the input and output tensors are aligned by the corner
points of their corner pixels, and the interpolation uses edge value padding
for out-of-boundary values, making this operation *independent* of input size
when `scale_factor` is kept the same. This only has an effect when `mode`
is `'linear'`, `'bilinear'`, `'bicubic'` or `'trilinear'`.
Default: `False`

Note

With `mode='bicubic'` or `mode='lanczos'`, it's possible to cause overshoot, in other words it can produce
negative values or values greater than 255 for images.
Explicitly call `result.clamp(min=0, max=255)` if you want to reduce the overshoot
when displaying the image.

Warning

With `align_corners = True`, the linearly interpolating modes
(linear, bilinear, and trilinear) don't proportionally align the
output and input pixels, and thus the output values can depend on the
input size. This was the default behavior for these modes up to version
0.3.1. Since then, the default behavior is `align_corners = False`.
See [`Upsample`](torch.nn.Upsample.html#torch.nn.Upsample) for concrete examples on how this
affects the outputs.