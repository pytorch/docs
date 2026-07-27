# BNReLU2d

*class*torch.ao.nn.intrinsic.BNReLU2d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/ao/nn/intrinsic/modules/fused.py#L218)

This is a sequential container which calls the BatchNorm 2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.