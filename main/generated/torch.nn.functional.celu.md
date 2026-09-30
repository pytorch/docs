# torch.nn.functional.celu

torch.nn.functional.celu(*input*, *alpha=1.*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/nn/functional.py#L1922)

Applies element-wise,
CELU(x)=max⁡(0,x)+min⁡(0,α∗(exp⁡(x/α)−1))\text{CELU}(x) = \max(0,x) + \min(0, \alpha * (\exp(x/\alpha) - 1))CELU(x)=max(0,x)+min(0,α∗(exp(x/α)−1)).

See [`CELU`](torch.nn.CELU.html#torch.nn.CELU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)