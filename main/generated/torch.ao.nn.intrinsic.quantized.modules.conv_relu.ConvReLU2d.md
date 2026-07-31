# ConvReLU2d

*class*torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L111)

A ConvReLU2d module is a fused module of Conv2d and ReLU

We adopt the same interface as [`torch.ao.nn.quantized.Conv2d`](torch.ao.nn.quantized.Conv2d.html#torch.ao.nn.quantized.Conv2d).

Variables:

**torch.ao.nn.quantized.Conv2d** (*Same as*) -

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L152)

Applies fused quantized Conv2d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L170)

Creates a quantized module from a float module.

*classmethod*from_reference(*ref_qconv*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L191)

Creates a quantized module from a reference module.