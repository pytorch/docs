# ConvTranspose2d

*class*torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *bias=True*, *dilation=1*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/ao/nn/quantized/dynamic/modules/conv.py#L368)

A dynamically quantized transposed convolution module with floating point tensors as inputs and outputs.

For details on input arguments, parameters, and implementation see
[`ConvTranspose2d`](torch.nn.ConvTranspose2d.html#torch.nn.ConvTranspose2d).

For special notes, please, see `Conv2d`

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`ConvTranspose2d`](torch.nn.ConvTranspose2d.html#torch.nn.ConvTranspose2d) for other attributes.

Examples:

```
>>> # With square kernels and equal stride
>>> m = nnq.ConvTranspose2d(16, 33, 3, stride=2)
>>> # non-square kernels and unequal stride and with padding
>>> m = nnq.ConvTranspose2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2))
>>> output = m(input)
>>> # exact output size can be also specified as an argument
>>> downsample = nnq.Conv2d(16, 16, 3, stride=2, padding=1)
>>> upsample = nnq.ConvTranspose2d(16, 16, 3, stride=2, padding=1)
>>> h = downsample(input)
>>> h.size()
torch.Size([1, 16, 6, 6])
>>> output = upsample(h, output_size=input.size())
>>> output.size()
torch.Size([1, 16, 12, 12])
```