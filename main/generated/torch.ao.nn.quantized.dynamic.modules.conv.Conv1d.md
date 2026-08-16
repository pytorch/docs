# Conv1d

*class*torch.ao.nn.quantized.dynamic.modules.conv.Conv1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*, *reduce_range=True*)[[source]](https://github.com/pytorch/pytorch/blob/8aac66fb022576e2d13144ab636372f686f23cfa/torch/ao/nn/quantized/dynamic/modules/conv.py#L28)

A dynamically quantized conv module with floating point tensors as inputs and outputs.

For details on input arguments, parameters, and implementation see
[`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and `Conv1d` and

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) for other attributes.

Examples:

```
>>> m = nn.quantized.dynamic.Conv1d(16, 33, 3, stride=2)
>>> input = torch.randn(20, 16, 100)
>>> output = m(input)
```