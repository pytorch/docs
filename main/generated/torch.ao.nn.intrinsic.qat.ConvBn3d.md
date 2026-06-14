# ConvBn3d

*class*torch.ao.nn.intrinsic.qat.ConvBn3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=None*, *padding_mode='zeros'*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/40e21dcd4b92d59842b3e3b7f542f855dedddb91/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L781)

A ConvBn3d module is a module fused from Conv3d and BatchNorm3d,
attached with FakeQuantize modules for weight,
used in quantization aware training.

We combined the interface of [`torch.nn.Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d) and
[`torch.nn.BatchNorm3d`](torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d).

Similar to [`torch.nn.Conv3d`](torch.nn.Conv3d.html#torch.nn.Conv3d), with FakeQuantize modules initialized
to default.

Variables:

- **freeze_bn** -
- **weight_fake_quant** - fake quant module for weight