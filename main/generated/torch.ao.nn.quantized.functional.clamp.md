# clamp

*class*torch.ao.nn.quantized.functional.clamp(*input*, *min_*, *max_*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/ao/nn/quantized/functional.py#L663)

float(input, min_, max_) -> Tensor

Applies the clamp function element-wise.
See `clamp` for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **min** - minimum value for clamping
- **max** - maximum value for clamping

Return type:

[*Tensor*](../tensors.html#torch.Tensor)