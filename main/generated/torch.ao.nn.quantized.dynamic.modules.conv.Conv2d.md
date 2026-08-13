# Conv2d

*class*torch.ao.nn.quantized.dynamic.modules.conv.Conv2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/nn/quantized/dynamic/modules/conv.py#L111)

A dynamically quantized conv module with floating point tensors as inputs and outputs.

For details on input arguments, parameters, and implementation see
[`Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d) and `Conv2d` and

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d) for other attributes.

Examples:

```
>>> # With square kernels and equal stride
>>> m = nn.quantized.dynamic.Conv2d(16, 33, 3, stride=2)
>>> # non-square kernels and unequal stride and with padding
>>> m = nn.quantized.dynamic.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2))
>>> # non-square kernels and unequal stride and with padding and dilation
>>> m = nn.quantized.dynamic.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1))
>>> input = torch.randn(20, 16, 50, 100)
>>> output = m(input)
```