# BNReLU3d

*class*torch.ao.nn.intrinsic.BNReLU3d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/nn/intrinsic/modules/fused.py#L235)

This is a sequential container which calls the BatchNorm 3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.