# torch.nn.functional.leaky_relu

torch.nn.functional.leaky_relu(*input*, *negative_slope=0.01*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/nn/functional.py#L1985)

Applies element-wise,
LeakyReLU(x)=max⁡(0,x)+negative_slope∗min⁡(0,x)\text{LeakyReLU}(x) = \max(0, x) + \text{negative\_slope} * \min(0, x)LeakyReLU(x)=max(0,x)+negative_slope∗min(0,x)

See [`LeakyReLU`](torch.nn.LeakyReLU.html#torch.nn.LeakyReLU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)