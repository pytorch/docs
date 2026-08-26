# Conv3d

*class*torch.ao.nn.quantized.dynamic.modules.conv.Conv3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/ao/nn/quantized/dynamic/modules/conv.py#L197)

A dynamically quantized conv module with floating point tensors as inputs and outputs.

For details on input arguments, parameters, and implementation see
[`Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) and `Conv3d` and

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) for other attributes.

Examples:

```
>>> # With square kernels and equal stride
>>> m = nn.quantized.dynamic.Conv3d(16, 33, 3, stride=2)
>>> # non-square kernels and unequal stride and with padding
>>> m = nn.quantized.dynamic.Conv3d(16, 33, (3, 5, 5), stride=(1, 2, 2), padding=(1, 2, 2))
>>> # non-square kernels and unequal stride and with padding and dilation
>>> m = nn.quantized.dynamic.Conv3d(16, 33, (3, 5, 5), stride=(1, 2, 2), padding=(1, 2, 2), dilation=(1, 2, 2))
>>> input = torch.randn(20, 16, 56, 56, 56)
>>> output = m(input)
```