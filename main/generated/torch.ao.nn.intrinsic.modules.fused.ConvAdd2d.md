# ConvAdd2d

*class*torch.ao.nn.intrinsic.modules.fused.ConvAdd2d(*conv*, *add*)[[source]](https://github.com/pytorch/pytorch/blob/be79392a0cedbbc0b5d2d3288173316425f90af4/torch/ao/nn/intrinsic/modules/fused.py#L295)

This is a sequential container which calls the Conv2d modules with extra Add.
During quantization this will be replaced with the corresponding fused module.

forward(*x1*, *x2*)[[source]](https://github.com/pytorch/pytorch/blob/be79392a0cedbbc0b5d2d3288173316425f90af4/torch/ao/nn/intrinsic/modules/fused.py#L303)

Applies convolution to x1 and adds the result to x2.