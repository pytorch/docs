# torch.nn.functional.selu

torch.nn.functional.selu(*input*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/784e50bb03d4ff5f8fdc368da8449558a8fb4a43/torch/nn/functional.py#L1865)

Applies element-wise,
SELU(x)=scale∗(max⁡(0,x)+min⁡(0,α∗(exp⁡(x)−1)))\text{SELU}(x) = scale * (\max(0,x) + \min(0, \alpha * (\exp(x) - 1)))SELU(x)=scale∗(max(0,x)+min(0,α∗(exp(x)−1))),
with α=1.6732632423543772848170429916717\alpha=1.6732632423543772848170429916717α=1.6732632423543772848170429916717 and
scale=1.0507009873554804934193349852946scale=1.0507009873554804934193349852946scale=1.0507009873554804934193349852946.

See [`SELU`](torch.nn.SELU.html#torch.nn.SELU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)