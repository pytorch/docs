# elu

*class*torch.ao.nn.quantized.functional.elu(*input*, *scale*, *zero_point*, *alpha=1.0*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/quantized/functional.py#L640)

This is the quantized version of [`elu()`](torch.nn.functional.elu.html#torch.nn.functional.elu).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)) - quantization scale of the output tensor
- **zero_point** ([*int*](https://docs.python.org/3/library/functions.html#int)) - quantization zero point of the output tensor
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the alpha constant

Return type:

[*Tensor*](../tensors.html#torch.Tensor)