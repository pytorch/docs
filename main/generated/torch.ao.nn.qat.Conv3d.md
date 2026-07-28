# Conv3d

*class*torch.ao.nn.qat.Conv3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/ao/nn/qat/modules/conv.py#L256)

A Conv3d module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as torch.nn.Conv3d, please see
[https://pytorch.org/docs/stable/nn.html?highlight=conv3d#torch.nn.Conv3d](https://pytorch.org/docs/stable/nn.html?highlight=conv3d#torch.nn.Conv3d)
for documentation.

Similar to torch.nn.Conv3d, with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight