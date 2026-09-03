# torch.nn.functional.upsample_bilinear

torch.nn.functional.upsample_bilinear(*input*, *size=None*, *scale_factor=None*)[[source]](https://github.com/pytorch/pytorch/blob/d7a82dcfcb838549a84f49516bc5c32ecf1eef90/torch/nn/functional.py#L5463)

Upsamples the input, using bilinear upsampling.

Warning

This function is deprecated in favor of [`torch.nn.functional.interpolate()`](torch.nn.functional.interpolate.html#torch.nn.functional.interpolate).
This is equivalent with
`nn.functional.interpolate(..., mode='bilinear', align_corners=True)`.

Expected inputs are spatial (4 dimensional). Use upsample_trilinear for
volumetric (5 dimensional) inputs.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - input
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial size.
- **scale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - multiplier for spatial size

Note

This operation may produce nondeterministic gradients when given tensors on a CUDA device. See [Reproducibility](../notes/randomness.html) for more information.