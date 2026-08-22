# torch.nn.functional.celu

torch.nn.functional.celu(*input*, *alpha=1.*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/nn/functional.py#L1922)

Applies element-wise,
CELU(x)=max⁡(0,x)+min⁡(0,α∗(exp⁡(x/α)−1))\text{CELU}(x) = \max(0,x) + \min(0, \alpha * (\exp(x/\alpha) - 1))CELU(x)=max(0,x)+min(0,α∗(exp(x/α)−1)).

See [`CELU`](torch.nn.CELU.html#torch.nn.CELU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)