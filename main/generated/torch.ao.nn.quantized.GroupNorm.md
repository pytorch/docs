# GroupNorm

*class*torch.ao.nn.quantized.GroupNorm(*num_groups*, *num_channels*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *affine=True*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/e708521bdf92712674ed3a0d332b56c356502328/torch/ao/nn/quantized/modules/normalization.py#L88)

This is the quantized version of [`GroupNorm`](torch.nn.GroupNorm.html#torch.nn.GroupNorm).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.