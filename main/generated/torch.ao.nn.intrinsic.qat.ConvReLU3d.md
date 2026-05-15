# ConvReLU3d

*class*torch.ao.nn.intrinsic.qat.ConvReLU3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L887)

A ConvReLU3d module is a fused module of Conv3d and ReLU, attached with
FakeQuantize modules for weight for
quantization aware training.

We combined the interface of [`Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) and
[`BatchNorm3d`](torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d).

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L936)

Performs forward pass through fused Conv3d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/211c61413d1f81c4a6ec8f1820328bef5cb24d86/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L942)

Creates a QAT module from a floating point module.