# ConvAdd2d

*class*torch.ao.nn.intrinsic.quantized.modules.conv_add.ConvAdd2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L12)

A ConvAdd2d module is a fused module of Conv2d and Add

We adopt the same interface as [`torch.ao.nn.quantized.Conv2d`](torch.ao.nn.quantized.Conv2d.html#torch.ao.nn.quantized.Conv2d).

Variables:

**torch.ao.nn.quantized.Conv2d** (*Same as*) -

forward(*input*, *extra_input*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L53)

Applies fused quantized Conv2d and addition.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L71)

Creates a quantized module from a float module.

*classmethod*from_reference(*ref_qconv*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/6f990b7ff484061525619d9776bb4c8174e00a4c/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L78)

Creates a quantized module from a reference module.