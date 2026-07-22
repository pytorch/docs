# ConvReLU1d

*class*torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L550)

A ConvReLU1d module is a fused module of Conv1d and ReLU, attached with
FakeQuantize modules for weight for
quantization aware training.

We combined the interface of [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and
[`BatchNorm1d`](torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d).

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L599)

Performs forward pass through fused Conv1d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L605)

Creates a QAT module from a floating point module.