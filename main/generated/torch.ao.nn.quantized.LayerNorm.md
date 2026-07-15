# LayerNorm

*class*torch.ao.nn.quantized.LayerNorm(*normalized_shape*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *elementwise_affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/ao/nn/quantized/modules/normalization.py#L14)

This is the quantized version of [`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.