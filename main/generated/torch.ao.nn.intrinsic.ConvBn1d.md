# ConvBn1d

*class*torch.ao.nn.intrinsic.ConvBn1d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/b5cf35aa75e0d5087ede9131ab2f970aa2de6509/torch/ao/nn/intrinsic/modules/fused.py#L110)

This is a sequential container which calls the Conv 1d and Batch Norm 1d modules.
During quantization this will be replaced with the corresponding fused module.