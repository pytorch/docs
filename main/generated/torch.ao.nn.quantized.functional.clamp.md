# clamp

*class*torch.ao.nn.quantized.functional.clamp(*input*, *min_*, *max_*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/ao/nn/quantized/functional.py#L660)

float(input, min_, max_) -> Tensor

Applies the clamp function element-wise.
See `clamp` for more details.

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **min** - minimum value for clamping
- **max** - maximum value for clamping

Return type:

[*Tensor*](../tensors.html#torch.Tensor)