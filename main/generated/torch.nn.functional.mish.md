# torch.nn.functional.mish

torch.nn.functional.mish(*input*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/nn/functional.py#L2406)

Apply the Mish function, element-wise.

Mish: A Self Regularized Non-Monotonic Neural Activation Function.

Mish(x)=x∗Tanh(Softplus(x))\text{Mish}(x) = x * \text{Tanh}(\text{Softplus}(x))

Mish(x)=x∗Tanh(Softplus(x))

Note

See [Mish: A Self Regularized Non-Monotonic Neural Activation Function](https://arxiv.org/abs/1908.08681)

See [`Mish`](torch.nn.Mish.html#torch.nn.Mish) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)