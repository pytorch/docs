# clamp

*class*torch.ao.nn.quantized.functional.clamp(*input*, *min_*, *max_*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/ao/nn/quantized/functional.py#L663)

float(input, min_, max_) -> Tensor

Applies the clamp function element-wise.
See `clamp` for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **min** - minimum value for clamping
- **max** - maximum value for clamping

Return type:

[*Tensor*](../tensors.html#torch.Tensor)