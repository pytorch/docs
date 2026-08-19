# torch.nn.functional.selu

torch.nn.functional.selu(*input*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/3af07571b9d7402fd74352d079e6ff5fa307ec5f/torch/nn/functional.py#L1893)

Applies element-wise,
SELU(x)=scale∗(max⁡(0,x)+min⁡(0,α∗(exp⁡(x)−1)))\text{SELU}(x) = scale * (\max(0,x) + \min(0, \alpha * (\exp(x) - 1)))SELU(x)=scale∗(max(0,x)+min(0,α∗(exp(x)−1))),
with α=1.6732632423543772848170429916717\alpha=1.6732632423543772848170429916717α=1.6732632423543772848170429916717 and
scale=1.0507009873554804934193349852946scale=1.0507009873554804934193349852946scale=1.0507009873554804934193349852946.

See [`SELU`](torch.nn.SELU.html#torch.nn.SELU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)