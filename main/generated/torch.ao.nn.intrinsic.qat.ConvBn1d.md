# ConvBn1d

*class*torch.ao.nn.intrinsic.qat.ConvBn1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=None*, *padding_mode='zeros'*, *eps=1e-05*, *momentum=0.1*, *freeze_bn=False*, *qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/b7ee7397ead012835c2d80ee53f64800630b1ab9/torch/ao/nn/intrinsic/qat/modules/conv_fused.py#L445)

A ConvBn1d module is a module fused from Conv1d and BatchNorm1d,
attached with FakeQuantize modules for weight,
used in quantization aware training.

We combined the interface of [`torch.nn.Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d) and
[`torch.nn.BatchNorm1d`](torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d).

Similar to [`torch.nn.Conv1d`](torch.nn.Conv1d.html#torch.nn.Conv1d), with FakeQuantize modules initialized
to default.

Variables:

- **freeze_bn** -
- **weight_fake_quant** - fake quant module for weight