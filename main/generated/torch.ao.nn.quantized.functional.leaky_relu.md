# leaky_relu

*class*torch.ao.nn.quantized.functional.leaky_relu(*input*, *negative_slope=0.01*, *inplace=False*, *scale=None*, *zero_point=None*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/ao/nn/quantized/functional.py#L556)

Quantized version of the.
leaky_relu(input, negative_slope=0.01, inplace=False, scale, zero_point) -> Tensor

Applies element-wise,
LeakyReLU(x)=max⁡(0,x)+negative_slope∗min⁡(0,x)\text{LeakyReLU}(x) = \max(0, x) + \text{negative\_slope} * \min(0, x)LeakyReLU(x)=max(0,x)+negative_slope∗min(0,x)

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Quantized input
- **negative_slope** ([*float*](https://docs.python.org/3/library/functions.html#float)) - The slope of the negative input
- **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) - Inplace modification of the input tensor
- **scale** ([*float*](https://docs.python.org/3/library/functions.html#float)*|**None*) - Scale and zero point of the output tensor.
- **zero_point** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - Scale and zero point of the output tensor.

See [`LeakyReLU`](torch.nn.LeakyReLU.html#torch.nn.LeakyReLU) for more details.