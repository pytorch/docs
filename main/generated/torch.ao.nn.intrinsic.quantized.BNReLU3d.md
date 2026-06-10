# BNReLU3d

*class*torch.ao.nn.intrinsic.quantized.BNReLU3d(*num_features*, *eps=1e-05*, *momentum=0.1*, *device=None*, *dtype=None*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L64)

A BNReLU3d module is a fused module of BatchNorm3d and ReLU

We adopt the same interface as [`torch.ao.nn.quantized.BatchNorm3d`](torch.ao.nn.quantized.BatchNorm3d.html#torch.ao.nn.quantized.BatchNorm3d).

Variables:

**torch.ao.nn.quantized.BatchNorm3d** (*Same as*) -

forward(*input*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L82)

Applies fused BatchNorm3d and ReLU.

*classmethod*from_float(*mod*, *use_precomputed_fake_quant=False*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L102)

Creates a quantized module from a float module.

*classmethod*from_reference(*bn_relu*, *output_scale*, *output_zero_point*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/ao/nn/intrinsic/quantized/modules/bn_relu.py#L110)

Creates a quantized module from a reference module.