# ConvReLU3d

*class*torch.ao.nn.intrinsic.quantized.ConvReLU3d(*in_channels*, *out_channels*, *kernel_size*, *stride=1*, *padding=0*, *dilation=1*, *groups=1*, *bias=True*, *padding_mode='zeros'*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/a7ff5691322735e9c4fc9f23bc19be9040aa9d50/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L201)

A ConvReLU3d module is a fused module of Conv3d and ReLU

We adopt the same interface as [`torch.ao.nn.quantized.Conv3d`](torch.ao.nn.quantized.Conv3d.html#torch.ao.nn.quantized.Conv3d).

Attributes: Same as torch.ao.nn.quantized.Conv3d

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/a7ff5691322735e9c4fc9f23bc19be9040aa9d50/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L243)

Applies fused quantized Conv3d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/a7ff5691322735e9c4fc9f23bc19be9040aa9d50/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L261)

Creates a quantized module from a float module.

*classmethod*from_reference(*ref_qconv*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/a7ff5691322735e9c4fc9f23bc19be9040aa9d50/torch/ao/nn/intrinsic/quantized/modules/conv_relu.py#L282)

Creates a quantized module from a reference module.