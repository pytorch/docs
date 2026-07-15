# GroupNorm

*class*torch.ao.nn.quantized.GroupNorm(*num_groups*, *num_channels*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/0f5932e5e82c3a4da21331c6cf7cddf6bce55cff/torch/ao/nn/quantized/modules/normalization.py#L88)

This is the quantized version of [`GroupNorm`](torch.nn.GroupNorm.html#torch.nn.GroupNorm).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.