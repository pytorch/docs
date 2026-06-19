# Conv3d

*class*torch.ao.nn.quantized.Conv3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/de1ad93d5279bade131efce3de7f798aef4faa3d/torch/ao/nn/quantized/modules/conv.py#L611)

Applies a 3D convolution over a quantized input signal composed of
several quantized input planes.

For details on input arguments, parameters, and implementation see
[`Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d).

Note

Only zeros is supported for the `padding_mode` argument.

Note

Only torch.quint8 is supported for the input data type.

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) for other attributes.

Examples:

```
>>> # With square kernels and equal stride
>>> m = nn.quantized.Conv3d(16, 33, 3, stride=2)
>>> # non-square kernels and unequal stride and with padding
>>> m = nn.quantized.Conv3d(16, 33, (3, 5, 5), stride=(1, 2, 2), padding=(1, 2, 2))
>>> # non-square kernels and unequal stride and with padding and dilation
>>> m = nn.quantized.Conv3d(16, 33, (3, 5, 5), stride=(1, 2, 2), padding=(1, 2, 2), dilation=(1, 2, 2))
>>> input = torch.randn(20, 16, 56, 56, 56)
>>> # quantize input to quint8
>>> q_input = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
>>> output = m(q_input)
```

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/de1ad93d5279bade131efce3de7f798aef4faa3d/torch/ao/nn/quantized/modules/conv.py#L730)

Creates a quantized module from a float module or qparams_dict.

Parameters:

**mod** ([*Module*](torch.nn.Module.html#torch.nn.Module)) - a float module, either produced by torch.ao.quantization
utilities or provided by the user