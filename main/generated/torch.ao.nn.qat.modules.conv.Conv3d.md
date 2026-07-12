# Conv3d

*class*torch.ao.nn.qat.modules.conv.Conv3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/ao/nn/qat/modules/conv.py#L256)

A Conv3d module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.Conv3d, please see
[https://pytorch.org/docs/stable/nn.html?highlight=conv3d#torch.nn.Conv3d](https://pytorch.org/docs/stable/nn.html?highlight=conv3d#torch.nn.Conv3d)
for documentation.

Similar to torch.nn.Conv3d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight