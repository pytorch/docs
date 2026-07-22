# ConvAddReLU2d

*class*torch.ao.nn.intrinsic.modules.fused.ConvAddReLU2d(*conv*, *add*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/modules/fused.py#L308)

This is a sequential container which calls the Conv2d, add, Relu.
During quantization this will be replaced with the corresponding fused module.

forward(*x1*, *x2*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/ao/nn/intrinsic/modules/fused.py#L317)

Applies convolution to x1, adds the result to x2, and applies ReLU.