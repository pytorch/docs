# hardswish

*class*torch.ao.nn.quantized.functional.hardswish(*input*, *scale*, *zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/2e9b4aff8d49b22bbebf288ccbf63983c51e45f0/torch/ao/nn/quantized/functional.py#L607)

This is the quantized version of [`hardswish()`](torch.nn.functional.hardswish.html#torch.nn.functional.hardswish).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **scale** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) - quantization scale of the output tensor
- **zero_point** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - quantization zero point of the output tensor

Return type:

[*Tensor*](../tensors.html#torch.Tensor)