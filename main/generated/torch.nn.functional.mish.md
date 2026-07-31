# torch.nn.functional.mish

torch.nn.functional.mish(*input*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/nn/functional.py#L2454)

Apply the Mish function, element-wise.

Mish: A Self Regularized Non-Monotonic Neural Activation Function.

Mish(x)=x∗Tanh(Softplus(x))\text{Mish}(x) = x * \text{Tanh}(\text{Softplus}(x))

Mish(x)=x∗Tanh(Softplus(x))

Note

See [Mish: A Self Regularized Non-Monotonic Neural Activation Function](https://arxiv.org/abs/1908.08681)

See [`Mish`](torch.nn.Mish.html#torch.nn.Mish) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)