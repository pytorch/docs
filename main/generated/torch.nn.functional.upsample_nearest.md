# torch.nn.functional.upsample_nearest

torch.nn.functional.upsample_nearest(*input*, *size=None*, *scale_factor=None*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/nn/functional.py#L5391)

Upsamples the input, using nearest neighbours' pixel values.

Warning

This function is deprecated in favor of [`torch.nn.functional.interpolate()`](torch.nn.functional.interpolate.html#torch.nn.functional.interpolate).
This is equivalent with `nn.functional.interpolate(..., mode='nearest')`.

Currently spatial and volumetric upsampling are supported (i.e. expected
inputs are 4 or 5 dimensional).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial
size.
- **scale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)) - multiplier for spatial size. Has to be an integer.

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.