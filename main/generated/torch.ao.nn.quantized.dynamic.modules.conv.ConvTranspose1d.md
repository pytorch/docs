# ConvTranspose1d

*class*torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *bias=True*, *dilation=1*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/ao/nn/quantized/dynamic/modules/conv.py#L285)

A dynamically quantized transposed convolution module with floating point tensors as inputs and outputs.

For details on input arguments, parameters, and implementation see
[`ConvTranspose1d`](torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d).

For special notes, please, see `Conv1d`

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`ConvTranspose1d`](torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d) for other attributes.

Examples:

```
>>> # With square kernels and equal stride
>>> m = nndq.ConvTranspose1d(16, 33, 3, stride=2)
>>> # non-square kernels and unequal stride and with padding
>>> m = nndq.ConvTranspose1d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2))
>>> output = m(input)
>>> # exact output size can be also specified as an argument
>>> downsample = nndq.Conv1d(16, 16, 3, stride=2, padding=1)
>>> upsample = nndq.ConvTranspose1d(16, 16, 3, stride=2, padding=1)
>>> h = downsample(input)
>>> h.size()
torch.Size([1, 16, 6])
>>> output = upsample(h, output_size=input.size())
>>> output.size()
torch.Size([1, 16, 12])
```