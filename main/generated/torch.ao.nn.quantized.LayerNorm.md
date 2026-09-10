# LayerNorm

*class*torch.ao.nn.quantized.LayerNorm(*normalized_shape*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *elementwise_affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/a62499b17156f49891b06593215215c6df2f94b4/torch/ao/nn/quantized/modules/normalization.py#L14)

This is the quantized version of [`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.