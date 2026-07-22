# threshold

*class*torch.ao.nn.quantized.functional.threshold(*input*, *threshold*, *value*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/quantized/functional.py#L617)

Applies the quantized version of the threshold function element-wise:

x={xif x>thresholdvalueotherwisex = \begin{cases}
 x & \text{if~} x > \text{threshold} \\
 \text{value} & \text{otherwise}
 \end{cases}

x={xvalue​if x>thresholdotherwise​

See [`Threshold`](torch.nn.Threshold.html#torch.nn.Threshold) for more details.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)