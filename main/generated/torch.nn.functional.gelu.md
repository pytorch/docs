# torch.nn.functional.gelu

torch.nn.functional.gelu(*input*, *approximate='none'*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/nn/functional.py#L2060)

When the approximate argument is 'none', it applies element-wise the function
GELU(x)=x∗Φ(x)\text{GELU}(x) = x * \Phi(x)GELU(x)=x∗Φ(x)

where Φ(x)\Phi(x)Φ(x) is the Cumulative Distribution Function for Gaussian Distribution.

When the approximate argument is 'tanh', Gelu is estimated with

GELU(x)=0.5∗x∗(1+Tanh(2/π∗(x+0.044715∗x3)))\text{GELU}(x) = 0.5 * x * (1 + \text{Tanh}(\sqrt{2 / \pi} * (x + 0.044715 * x^3)))

GELU(x)=0.5∗x∗(1+Tanh(2/π​∗(x+0.044715∗x3)))

See [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415).