# clamp

*class*torch.ao.nn.quantized.functional.clamp(*input*, *min_*, *max_*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/nn/quantized/functional.py#L663)

float(input, min_, max_) -> Tensor

Applies the clamp function element-wise.
See `clamp` for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **min** - minimum value for clamping
- **max** - maximum value for clamping

Return type:

[*Tensor*](../tensors.html#torch.Tensor)