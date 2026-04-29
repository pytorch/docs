# ConvReLU1d

*class*torch.ao.nn.intrinsic.quantized.ConvReLU1d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L21)

A ConvReLU1d module is a fused module of Conv1d and ReLU

We adopt the same interface as [`torch.ao.nn.quantized.Conv1d`](torch.ao.nn.quantized.Conv1d.html#torch.ao.nn.quantized.Conv1d).

Variables:

**torch.ao.nn.quantized.Conv1d** (*Same as*) -

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L63)

Applies fused quantized Conv1d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L82)

Creates a quantized module from a float module.

*classmethod*from_reference(*ref_qconv*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L101)

Creates a quantized module from a reference module.