# ConvReLU3d

*class*torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L887)

A ConvReLU3d module is a fused module of Conv3d and ReLU, attached with
FakeQuantize modules for weight for
quantization aware training.

We combined the interface of [`Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) and
[`ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L936)

Performs forward pass through fused Conv3d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/6421eecbd685d270304ca7e0136286a344319752/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L942)

Creates a QAT module from a floating point module.