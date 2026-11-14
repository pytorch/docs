# ConvBnReLU2d

*class*torch.ao.nn.intrinsic.ConvBnReLU2d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/ao/nn/intrinsic/modules/fused.py#L163)

This is a sequential container which calls the Conv 2d, Batch Norm 2d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.