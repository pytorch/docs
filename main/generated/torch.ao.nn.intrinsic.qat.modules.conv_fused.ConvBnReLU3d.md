# ConvBnReLU3d

*class*torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=None*, *padding_mode='zeros'*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L851)

A ConvBnReLU3d module is a module fused from Conv3d, BatchNorm3d and ReLU,
attached with FakeQuantize modules for weight,
used in quantization aware training.

We combined the interface of [`torch.nn.Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) and
[`torch.nn.BatchNorm3d`](torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d) and [`torch.nn.ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Similar to torch.nn.Conv3d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L875)

Performs forward pass through fused Conv3d, BatchNorm3d, and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L879)

Creates a QAT module from a floating point module.