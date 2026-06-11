# torch.nn.functional.leaky_relu

torch.nn.functional.leaky_relu(*input*, *negative_slope=0.01*, *inplace=False*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/nn/functional.py#L1949)

Applies element-wise,
LeakyReLU(x)=max⁡(0,x)+negative_slope∗min⁡(0,x)\text{LeakyReLU}(x) = \max(0, x) + \text{negative\_slope} * \min(0, x)LeakyReLU(x)=max(0,x)+negative_slope∗min(0,x)

See [`LeakyReLU`](torch.nn.LeakyReLU.html#torch.nn.LeakyReLU) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)