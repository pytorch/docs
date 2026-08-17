# torch.nn.functional.silu

torch.nn.functional.silu(*input*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/nn/functional.py#L2429)

Apply the Sigmoid Linear Unit (SiLU) function, element-wise.

The SiLU function is also known as the swish function.

silu(x)=x∗σ(x),where σ(x) is the logistic sigmoid.\text{silu}(x) = x * \sigma(x), \text{where } \sigma(x) \text{ is the logistic sigmoid.}

silu(x)=x∗σ(x),where σ(x) is the logistic sigmoid.

Note

See [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415)
where the SiLU (Sigmoid Linear Unit) was originally coined, and see
[Sigmoid-Weighted Linear Units for Neural Network Function Approximation
in Reinforcement Learning](https://arxiv.org/abs/1702.03118) and [Swish:
a Self-Gated Activation Function](https://arxiv.org/abs/1710.05941v1)
where the SiLU was experimented with later.

See [`SiLU`](torch.nn.SiLU.html#torch.nn.SiLU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)