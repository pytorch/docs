# LayerNorm

*class*torch.ao.nn.quantized.LayerNorm(*normalized_shape*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *elementwise_affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/ao/nn/quantized/modules/normalization.py#L14)

This is the quantized version of [`LayerNorm`](torch.nn.LayerNorm.html#torch.nn.LayerNorm).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.