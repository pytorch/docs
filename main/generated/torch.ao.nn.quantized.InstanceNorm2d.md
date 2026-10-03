# InstanceNorm2d

*class*torch.ao.nn.quantized.InstanceNorm2d(*num_features*, *weight*, *bias*, *scale*, *zero_point*, *eps=1e-05*, *momentum=0.1*, *affine=False*, *track_running_stats=False*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/ao/nn/quantized/modules/normalization.py#L216)

This is the quantized version of [`InstanceNorm2d`](torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d).

Additional args:

- **scale** - quantization scale of the output, type: double.
- **zero_point** - quantization zero point of the output, type: long.