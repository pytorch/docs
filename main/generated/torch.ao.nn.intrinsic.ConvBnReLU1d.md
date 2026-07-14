# ConvBnReLU1d

*class*torch.ao.nn.intrinsic.ConvBnReLU1d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/b251a9ea25c953bfac6da40dfc57f259e2b120ee/torch/ao/nn/intrinsic/modules/fused.py#L144)

This is a sequential container which calls the Conv 1d, Batch Norm 1d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.