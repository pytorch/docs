# torch.nn.functional.leaky_relu

torch.nn.functional.leaky_relu(*input*, *negative_slope=0.01*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/1b51ed6169475ed863f4ee43b7eaa52ecda0f862/torch/nn/functional.py#L1985)

Applies element-wise,
LeakyReLU(x)=max⁡(0,x)+negative_slope∗min⁡(0,x)\text{LeakyReLU}(x) = \max(0, x) + \text{negative\_slope} * \min(0, x)LeakyReLU(x)=max(0,x)+negative_slope∗min(0,x)

See [`LeakyReLU`](torch.nn.LeakyReLU.html#torch.nn.LeakyReLU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)