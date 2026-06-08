# hardswish

*class*torch.ao.nn.quantized.functional.hardswish(*input*, *scale*, *zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/nn/quantized/functional.py#L604)

This is the quantized version of [`hardswish()`](torch.nn.functional.hardswish.html#torch.nn.functional.hardswish).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)) - quantization scale of the output tensor
- **zero_point** ([*int*](https://docs.python.org/3/library/functions.html#int)) - quantization zero point of the output tensor

Return type:

[*Tensor*](../tensors.html#torch.Tensor)