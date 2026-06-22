# Conv2d

*class*torch.ao.nn.qat.modules.conv.Conv2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/ao/nn/qat/modules/conv.py#L191)

A Conv2d module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.Conv2d, please see
[https://pytorch.org/docs/stable/nn.html?highlight=conv2d#torch.nn.Conv2d](https://pytorch.org/docs/stable/nn.html?highlight=conv2d#torch.nn.Conv2d)
for documentation.

Similar to torch.nn.Conv2d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight