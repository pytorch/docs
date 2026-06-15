# LayerNorm

*class*torch.ao.nn.quantized.LayerNorm(*normalized_shape*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *elementwise_affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/nn/quantized/modules/normalization.py#L14)

This is the quantized version of [`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.