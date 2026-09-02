# ConvReLU1d

*class*torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L550)

A ConvReLU1d module is a fused module of Conv1d and ReLU, attached with
FakeQuantize modules for weight for
quantization aware training.

We combined the interface of [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and
[`ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L599)

Performs forward pass through fused Conv1d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L605)

Creates a QAT module from a floating point module.