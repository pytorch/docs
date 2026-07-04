# ConvTranspose3d

*class*torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *bias=True*, *dilation=1*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/9a3243ec510ddea6c63c86d01aef273f400f375f/torch/ao/nn/quantized/dynamic/modules/conv.py#L451)

A dynamically quantized transposed convolution module with floating point tensors as inputs and outputs.

For details on input arguments, parameters, and implementation see
[`ConvTranspose3d`](torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d).

For special notes, please, see `Conv3d`

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`ConvTranspose3d`](torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) for other attributes.

Examples:

```
>>> # With cubic kernels and equal stride
>>> m = nnq.ConvTranspose3d(16, 33, 3, stride=2)
>>> # non-cubic kernels and unequal stride and with padding
>>> m = nnq.ConvTranspose3d(16, 33, (3, 3, 5), stride=(2, 1, 1), padding=(4, 2, 2))
>>> output = m(input)
>>> # exact output size can be also specified as an argument
>>> downsample = nnq.Conv3d(16, 16, 3, stride=2, padding=1)
>>> upsample = nnq.ConvTranspose3d(16, 16, 3, stride=2, padding=1)
>>> h = downsample(input)
>>> h.size()
torch.Size([1, 16, 6, 6, 6])
>>> output = upsample(h, output_size=input.size())
>>> output.size()
torch.Size([1, 16, 12, 12, 12])
```