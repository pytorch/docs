# BNReLU3d

*class*torch.ao.nn.intrinsic.BNReLU3d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/nn/intrinsic/modules/fused.py#L235)

This is a sequential container which calls the BatchNorm 3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.