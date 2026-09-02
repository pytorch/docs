# ConvAdd2d

*class*torch.ao.nn.intrinsic.modules.fused.ConvAdd2d(*conv*, *add*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/intrinsic/modules/fused.py#L295)

This is a sequential container which calls the Conv2d modules with extra Add.
During quantization this will be replaced with the corresponding fused module.

forward(*x1*, *x2*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/ao/nn/intrinsic/modules/fused.py#L303)

Applies convolution to x1 and adds the result to x2.