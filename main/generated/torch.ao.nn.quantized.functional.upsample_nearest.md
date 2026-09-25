# upsample_nearest

*class*torch.ao.nn.quantized.functional.upsample_nearest(*input*, *size=None*, *scale_factor=None*)[[source]](https://github.com/pytorch/pytorch/blob/5eb87fdd0ab88b4b6cc91ec5bfcf4de22d6a6c49/torch/ao/nn/quantized/functional.py#L762)

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
- **size** ([*int*](https://docs.python.org/3/builtins/functions.html#int)*or**Tuple**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*] or**Tuple**[*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*,*[*int*](https://docs.python.org/3/builtins/functions.html#int)*]*) - output spatial
size.
- **scale_factor** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - multiplier for spatial size. Has to be an integer.