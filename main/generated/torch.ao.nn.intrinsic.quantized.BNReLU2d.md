# BNReLU2d

*class*torch.ao.nn.intrinsic.quantized.BNReLU2d(*num_features*, *eps=1e-05*, *momentum=0.1*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L12)

A BNReLU2d module is a fused module of BatchNorm2d and ReLU

We adopt the same interface as [`torch.ao.nn.quantized.BatchNorm2d`](torch.ao.nn.quantized.BatchNorm2d.html#torch.ao.nn.quantized.BatchNorm2d).

Variables:

**torch.ao.nn.quantized.BatchNorm2d** (*Same as*) -

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L30)

Applies fused BatchNorm2d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L50)

Creates a quantized module from a float module.

*classmethod*from_reference(*bn_relu*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L58)

Creates a quantized module from a reference module.