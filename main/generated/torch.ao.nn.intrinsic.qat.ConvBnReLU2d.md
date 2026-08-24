# ConvBnReLU2d

*class*torch.ao.nn.intrinsic.qat.ConvBnReLU2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=None*, *padding_mode='zeros'*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L683)

A ConvBnReLU2d module is a module fused from Conv2d, BatchNorm2d and ReLU,
attached with FakeQuantize modules for weight,
used in quantization aware training.

We combined the interface of [`torch.nn.Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d) and
[`torch.nn.BatchNorm2d`](torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d) and [`torch.nn.ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Similar to torch.nn.Conv2d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L708)

Performs forward pass through fused Conv2d, BatchNorm2d, and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L712)

Creates a QAT module from a floating point module.