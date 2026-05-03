# ConvBnReLU3d

*class*torch.ao.nn.intrinsic.ConvBnReLU3d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/ao/nn/intrinsic/modules/fused.py#L199)

This is a sequential container which calls the Conv 3d, Batch Norm 3d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.