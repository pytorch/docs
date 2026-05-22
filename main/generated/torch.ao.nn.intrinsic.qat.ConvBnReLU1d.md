# ConvBnReLU1d

*class*torch.ao.nn.intrinsic.qat.ConvBnReLU1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=None*, *padding_mode='zeros'*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L515)

A ConvBnReLU1d module is a module fused from Conv1d, BatchNorm1d and ReLU,
attached with FakeQuantize modules for weight,
used in quantization aware training.

We combined the interface of [`torch.nn.Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and
[`torch.nn.BatchNorm1d`](torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d) and [`torch.nn.ReLU`](torch.nn.ReLU.html#torch.nn.ReLU).

Similar to torch.nn.Conv1d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L540)

Performs forward pass through fused Conv1d, BatchNorm1d, and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L544)

Creates a QAT module from a floating point module.