# torch.nn.functional.interpolate

torch.nn.functional.interpolate(*input*, *size=None*, *scale_factor=None*, *mode='nearest'*, *align_corners=None*, *recompute_scale_factor=None*, *antialias=False*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/nn/functional.py#L4775)

Down/up samples the input.

Tensor interpolated to either the given `size` or the given
`scale_factor`

The algorithm used for interpolation is determined by `mode`.

Currently temporal, spatial and volumetric sampling are supported, i.e.
expected inputs are 3-D, 4-D or 5-D in shape.

The input dimensions are interpreted in the form:
mini-batch x channels x [optional depth] x [optional height] x width.

The modes available for resizing are: nearest, linear (3D-only),
bilinear, bicubic (4D-only), trilinear (5D-only), lanczos (4D-only, CPU only), area, nearest-exact

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - the input tensor
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial size.
- **scale_factor** ([*float*](https://docs.python.org/3/library/functions.html#float)*or**Tuple**[*[*float*](https://docs.python.org/3/library/functions.html#float)*]*) - multiplier for spatial size. If scale_factor is a tuple,
its length has to match the number of spatial dimensions; input.dim() - 2.
- **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - algorithm used for upsampling:
`'nearest'` | `'linear'` | `'bilinear'` | `'bicubic'` |
`'trilinear'` | `'lanczos'` | `'area'` | `'nearest-exact'`. Default: `'nearest'`
- **align_corners** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - Geometrically, we consider the pixels of the
input and output as squares rather than points.
If set to `True`, the input and output tensors are aligned by the
center points of their corner pixels, preserving the values at the corner pixels.
If set to `False`, the input and output tensors are aligned by the corner
points of their corner pixels, and the interpolation uses edge value padding
for out-of-boundary values, making this operation *independent* of input size
when `scale_factor` is kept the same. This only has an effect when `mode`
is `'linear'`, `'bilinear'`, `'bicubic'` or `'trilinear'`.
Default: `None`. `None` leaves `align_corners` unset for modes
that do not use it. For modes that use `align_corners`, `None`
is treated as `False`.
- **recompute_scale_factor** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - recompute the scale_factor for use in the
interpolation calculation. If recompute_scale_factor is `True`, then
scale_factor must be passed in and scale_factor is used to compute the
output size. The computed output size will be used to infer new scales for
the interpolation. Note that when scale_factor is floating-point, it may differ
from the recomputed scale_factor due to rounding and precision issues.
If recompute_scale_factor is `False`, then size or scale_factor will
be used directly for interpolation. Default: `None`.
- **antialias** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - flag to apply anti-aliasing. Default: `False`. Using anti-alias
option together with `align_corners=False`, interpolation result would match Pillow
result for downsampling operation. Supported modes: `'bilinear'`, `'bicubic'`, `'lanczos'`.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Note

With `mode='bicubic'` or `mode='lanczos'`, it's possible to cause overshoot. For some dtypes, it can produce
negative values or values greater than 255 for images. Explicitly call `result.clamp(min=0,max=255)`
if you want to reduce the overshoot when displaying the image.
For `uint8` inputs, it already performs saturating cast operation. So, no manual clamp operation is needed.

Note

Mode `mode='lanczos'` uses a Lanczos-3 windowed sinc filter (6 taps) and requires
`antialias=True`. It only supports 4-D input (i.e. 2D spatial) and CPU. With `antialias=True`
and `align_corners=False`, the result matches PIL's `Image.LANCZOS` resampling filter.

Note

Mode `mode='nearest-exact'` matches Scikit-Image and PIL nearest neighbours interpolation
algorithms and fixes known issues with `mode='nearest'`. This mode is introduced to keep
backward compatibility.
Mode `mode='nearest'` matches buggy OpenCV's `INTER_NEAREST` interpolation algorithm.

Note

The gradients for the dtype `float16` on CUDA may be inaccurate in the upsample operation
when using modes `['linear', 'bilinear', 'bicubic', 'trilinear', 'area']`.
For more details, please refer to the discussion in
[issue#104157](https://github.com/pytorch/pytorch/issues/104157).

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.