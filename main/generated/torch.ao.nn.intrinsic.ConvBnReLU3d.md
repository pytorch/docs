# ConvBnReLU3d

*class*torch.ao.nn.intrinsic.ConvBnReLU3d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/502e93eb52e0fcf07a908796ccd61af06c4b58b9/torch/ao/nn/intrinsic/modules/fused.py#L199)

This is a sequential container which calls the Conv 3d, Batch Norm 3d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.