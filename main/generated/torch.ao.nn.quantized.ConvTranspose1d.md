# ConvTranspose1d

*class*torch.ao.nn.quantized.ConvTranspose1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *output_padding=0*, *groups=1*, *bias=True*, *dilation=1*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/ao/nn/quantized/modules/conv.py#L877)

Applies a 1D transposed convolution operator over an input image
composed of several input planes.
For details on input arguments, parameters, and implementation see
[`ConvTranspose1d`](torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d).

Note

Currently only the QNNPACK engine is implemented.
Please, set the torch.backends.quantized.engine = 'qnnpack'

For special notes, please, see [`Conv1d`](torch.ao.nn.quantized.Conv1d.html#torch.ao.nn.quantized.Conv1d)

Variables:

- **weight** ([*Tensor*](../tensors.html#torch.Tensor)) - packed tensor derived from the learnable weight
parameter.
- **scale** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output scale
- **zero_point** ([*Tensor*](../tensors.html#torch.Tensor)) - scalar for the output zero point

See [`ConvTranspose2d`](torch.nn.ConvTranspose2d.html#torch.nn.ConvTranspose2d) for other attributes.

Examples:

```
>>> torch.backends.quantized.engine = 'qnnpack'
>>> from torch.ao.nn import quantized as nnq
>>> # With square kernels and equal stride
>>> m = nnq.ConvTranspose1d(16, 33, 3, stride=2)
>>> # non-square kernels and unequal stride and with padding
>>> m = nnq.ConvTranspose1d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2))
>>> input = torch.randn(20, 16, 50)
>>> q_input = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
>>> output = m(q_input)
>>> # exact output size can be also specified as an argument
>>> input = torch.randn(1, 16, 12)
>>> q_input = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
>>> downsample = nnq.Conv1d(16, 16, 3, stride=2, padding=1)
>>> upsample = nnq.ConvTranspose1d(16, 16, 3, stride=2, padding=1)
>>> h = downsample(q_input)
>>> h.size()
torch.Size([1, 16, 6])
>>> output = upsample(h, output_size=input.size())
>>> output.size()
torch.Size([1, 16, 12])
```