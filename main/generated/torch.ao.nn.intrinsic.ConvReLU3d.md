# ConvReLU3d

*class*torch.ao.nn.intrinsic.ConvReLU3d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/7438967adaaabe37e14e1d7d26e1ab5ed2ed9054/torch/ao/nn/intrinsic/modules/fused.py#L76)

This is a sequential container which calls the Conv3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.