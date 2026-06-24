# ConvAddReLU2d

*class*torch.ao.nn.intrinsic.modules.fused.ConvAddReLU2d(*conv*, *add*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/ao/nn/intrinsic/modules/fused.py#L308)

This is a sequential container which calls the Conv2d, add, Relu.
During quantization this will be replaced with the corresponding fused module.

forward(*x1*, *x2*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/ao/nn/intrinsic/modules/fused.py#L317)

Applies convolution to x1, adds the result to x2, and applies ReLU.