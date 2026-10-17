# ConvBnReLU2d

*class*torch.ao.nn.intrinsic.ConvBnReLU2d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/64cf21712548b5b1ea993d13784345169fb72869/torch/ao/nn/intrinsic/modules/fused.py#L163)

This is a sequential container which calls the Conv 2d, Batch Norm 2d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.