# upsample_nearest

*class*torch.ao.nn.quantized.functional.upsample_nearest(*input*, *size=None*, *scale_factor=None*)[[source]](https://github.com/pytorch/pytorch/blob/a37249c7e9824d557710fe7682d943593ef355d8/torch/ao/nn/quantized/functional.py#L759)

Upsamples the input, using nearest neighbours' pixel values.

Warning

This function is deprecated in favor of
[`torch.ao.nn.quantized.functional.interpolate()`](torch.ao.nn.quantized.functional.interpolate.html#torch.ao.nn.quantized.functional.interpolate).
This is equivalent with `nn.quantized.functional.interpolate(..., mode='nearest')`.

Note

The input quantization parameters propagate to the output.

Note

Only 2D inputs are supported

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial
size.
- **scale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)) - multiplier for spatial size. Has to be an integer.