# threshold

*class*torch.ao.nn.quantized.functional.threshold(*input*, *threshold*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/ao/nn/quantized/functional.py#L620)

Applies the quantized version of the threshold function element-wise:

x={xif x>thresholdvalueotherwisex = \begin{cases}
 x & \text{if~} x > \text{threshold} \\
 \text{value} & \text{otherwise}
 \end{cases}

x={xvalue​if x>thresholdotherwise​

See [`Threshold`](torch.nn.Threshold.html#torch.nn.Threshold) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)