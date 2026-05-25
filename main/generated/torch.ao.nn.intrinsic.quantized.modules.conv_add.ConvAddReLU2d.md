# ConvAddReLU2d

*class*torch.ao.nn.intrinsic.quantized.modules.conv_add.ConvAddReLU2d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L84)

A ConvAddReLU2d module is a fused module of Conv2d, Add and Relu

We adopt the same interface as [`torch.ao.nn.quantized.Conv2d`](torch.ao.nn.quantized.Conv2d.html#torch.ao.nn.quantized.Conv2d).

Variables:

**torch.ao.nn.quantized.Conv2d** (*Same as*) -

forward(*input*, *extra_input*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L125)

Applies fused quantized Conv2d, addition, and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L143)

Creates a quantized module from a float module.

*classmethod*from_reference(*ref_qconv*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/69bbaeafe0b3f1e423be17b25ca11b149845b521/torch/ao/nn/intrinsic/quantized/modules/conv_add.py#L150)

Creates a quantized module from a reference module.