# linear

*class*torch.ao.nn.quantized.functional.linear(*input*, *weight*, *bias=None*, *scale=None*, *zero_point=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/ao/nn/quantized/functional.py#L438)

Applies a linear transformation to the incoming quantized data:
y=xAT+by = xA^T + by=xAT+b.
See [`Linear`](torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear)

Note

Current implementation packs weights on every call, which has penalty on performance.
If you want to avoid the overhead, use [`Linear`](torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear).

Parameters:

- **input** ([*Tensor*](../tensors.html#torch.Tensor)) - Quantized input of type torch.quint8
- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - Quantized weight of type torch.qint8
- **bias** ([*Tensor*](../tensors.html#torch.Tensor)) - None or fp32 bias of type torch.float
- **scale** (*double*) - output scale. If None, derived from the input scale
- **zero_point** (*python:long*) - output zero point. If None, derived from the input zero_point

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

Shape:

- Input: (N,∗,in_features)(N, *, in\_features)(N,∗,in_features) where * means any number of
additional dimensions
- Weight: (out_features,in_features)(out\_features, in\_features)(out_features,in_features)
- Bias: (out_features)(out\_features)(out_features)
- Output: (N,∗,out_features)(N, *, out\_features)(N,∗,out_features)