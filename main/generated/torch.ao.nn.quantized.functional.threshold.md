# threshold

*class*torch.ao.nn.quantized.functional.threshold(*input*, *threshold*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/ao/nn/quantized/functional.py#L617)

Applies the quantized version of the threshold function element-wise:

x={xif x>thresholdvalueotherwisex = \begin{cases}
 x & \text{if~} x > \text{threshold} \\
 \text{value} & \text{otherwise}
 \end{cases}

x={xvalue​if x>thresholdotherwise​

See [`Threshold`](torch.nn.Threshold.html#torch.nn.Threshold) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)