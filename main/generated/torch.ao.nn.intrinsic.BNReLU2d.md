# BNReLU2d

*class*torch.ao.nn.intrinsic.BNReLU2d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/ao/nn/intrinsic/modules/fused.py#L218)

This is a sequential container which calls the BatchNorm 2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.