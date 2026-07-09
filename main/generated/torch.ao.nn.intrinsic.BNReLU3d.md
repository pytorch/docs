# BNReLU3d

*class*torch.ao.nn.intrinsic.BNReLU3d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/7a37a01092627acd59ddfcb9cefe5a578f5f6996/torch/ao/nn/intrinsic/modules/fused.py#L235)

This is a sequential container which calls the BatchNorm 3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.