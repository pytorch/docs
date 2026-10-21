# ConvBnReLU3d

*class*torch.ao.nn.intrinsic.ConvBnReLU3d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/1404563568be4b2d23634a409bd7a9c7972c1c5c/torch/ao/nn/intrinsic/modules/fused.py#L199)

This is a sequential container which calls the Conv 3d, Batch Norm 3d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.