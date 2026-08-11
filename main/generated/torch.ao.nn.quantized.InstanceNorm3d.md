# InstanceNorm3d

*class*torch.ao.nn.quantized.InstanceNorm3d(*num_features*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *momentum=0.1*, *affine=False*, *track_running_stats=False*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/ab02f71479d3b0fb41d5b722bbe1943340f2022b/torch/ao/nn/quantized/modules/normalization.py#L283)

This is the quantized version of [`InstanceNorm3d`](torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.