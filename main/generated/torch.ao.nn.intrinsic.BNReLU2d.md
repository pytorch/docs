# BNReLU2d

*class*torch.ao.nn.intrinsic.BNReLU2d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/b7954b2399da4803024b9a2850e39c588522015f/torch/ao/nn/intrinsic/modules/fused.py#L218)

This is a sequential container which calls the BatchNorm 2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.