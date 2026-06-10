# ConvBn2d

*class*torch.ao.nn.intrinsic.qat.ConvBn2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=None*, *padding_mode='zeros'*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L613)

A ConvBn2d module is a module fused from Conv2d and BatchNorm2d,
attached with FakeQuantize modules for weight,
used in quantization aware training.

We combined the interface of [`torch.nn.Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d) and
[`torch.nn.BatchNorm2d`](torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d).

Similar to [`torch.nn.Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d), with FakeQuantize modules initialized
to default.

Variables:

- **freeze_bn** -
- **weight_fake_quant** - fake quant module for weight