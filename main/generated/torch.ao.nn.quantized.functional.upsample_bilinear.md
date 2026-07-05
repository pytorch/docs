# upsample_bilinear

*class*torch.ao.nn.quantized.functional.upsample_bilinear(*input*, *size=None*, *scale_factor=None*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/ao/nn/quantized/functional.py#L733)

Upsamples the input, using bilinear upsampling.

Warning

This function is deprecated in favor of
[`torch.ao.nn.quantized.functional.interpolate()`](torch.ao.nn.quantized.functional.interpolate.html#torch.ao.nn.quantized.functional.interpolate).
This is equivalent with
`nn.quantized.functional.interpolate(..., mode='bilinear', align_corners=True)`.

Note

The input quantization parameters propagate to the output.

Note

Only 2D inputs are supported

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **size** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - output spatial size.
- **scale_factor** ([*int*](https://docs.python.org/3/library/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - multiplier for spatial size