# elu

*class*torch.ao.nn.quantized.functional.elu(*input*, *scale*, *zero_point*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/ao/nn/quantized/functional.py#L637)

This is the quantized version of [`elu()`](torch.nn.functional.elu.html#torch.nn.functional.elu).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)) - quantization scale of the output tensor
- **zero_point** ([*int*](https://docs.python.org/3/library/functions.html#int)) - quantization zero point of the output tensor
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the alpha constant

Return type:

[*Tensor*](../tensors.html#torch.Tensor)