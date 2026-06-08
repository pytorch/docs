# celu

*class*torch.ao.nn.quantized.functional.celu(*input*, *scale*, *zero_point*, *alpha=1.*)[[source]](https://github.com/pytorch/pytorch/blob/411c8477fa2478b2318f3823d57cf684a3a1f389/torch/ao/nn/quantized/functional.py#L539)

Applies the quantized CELU function element-wise.

CELU(x)=max⁡(0,x)+min⁡(0,α∗(exp⁡(x/α)−1))\text{CELU}(x) = \max(0,x) + \min(0, \alpha * (\exp(x / \alpha) - 1))

CELU(x)=max(0,x)+min(0,α∗(exp(x/α)−1))
Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - quantized input
- **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) - the α\alphaα value for the CELU formulation. Default: 1.0

Return type:

[*Tensor*](../tensors.html#torch.Tensor)