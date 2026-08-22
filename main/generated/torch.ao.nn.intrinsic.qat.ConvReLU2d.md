# ConvReLU2d

*class*torch.ao.nn.intrinsic.qat.ConvReLU2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L718)

A ConvReLU2d module is a fused module of Conv2d and ReLU, attached with
FakeQuantize modules for weight for
quantization aware training.

We combined the interface of [`Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d) and
[`ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L767)

Performs forward pass through fused Conv2d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L773)

Creates a QAT module from a floating point module.