# Conv1d

*class*torch.ao.nn.qat.modules.conv.Conv1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *qconfig=None*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/007b142ea0da19b2a8b4c33c2544b0c2f459e7fc/torch/ao/nn/qat/modules/conv.py#L131)

A Conv1d module attached with FakeQuantize modules for weight,
used for quantization aware training.

We adopt the same interface as [`Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d)

Similar to [`Conv2d`](torch.nn.Conv2d.html#torch.nn.Conv2d), with FakeQuantize modules initialized to
default.

Variables:

**weight_fake_quant** - fake quant module for weight