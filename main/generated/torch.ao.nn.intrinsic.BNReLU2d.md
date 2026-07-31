# BNReLU2d

*class*torch.ao.nn.intrinsic.BNReLU2d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/nn/intrinsic/modules/fused.py#L218)

This is a sequential container which calls the BatchNorm 2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.