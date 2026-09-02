# InstanceNorm2d

*class*torch.ao.nn.quantized.InstanceNorm2d(*num_features*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *momentum=0.1*, *affine=False*, *track_running_stats=False*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/quantized/modules/normalization.py#L216)

This is the quantized version of [`InstanceNorm2d`](torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.