# Conv3d

*class*torch.ao.nn.qat.modules.conv.Conv3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/9a3243ec510ddea6c63c86d01aef273f400f375f/torch/ao/nn/qat/modules/conv.py#L256)

A Conv3d module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.Conv3d, please see
[https://pytorch.org/docs/stable/nn.html?highlight=conv3d#torch.nn.Conv3d](https://pytorch.org/docs/stable/nn.html?highlight=conv3d#torch.nn.Conv3d)
for documentation.

Similar to torch.nn.Conv3d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight