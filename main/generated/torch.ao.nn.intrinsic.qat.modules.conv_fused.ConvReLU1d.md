# ConvReLU1d

*class*torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L550)

A ConvReLU1d module is a fused module of Conv1d and ReLU, attached with
FakeQuantize modules for weight for
quantization aware training.

We combined the interface of [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and
[`ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L599)

Performs forward pass through fused Conv1d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L605)

Creates a QAT module from a floating point module.