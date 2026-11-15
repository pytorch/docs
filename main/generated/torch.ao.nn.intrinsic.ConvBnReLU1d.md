# ConvBnReLU1d

*class*torch.ao.nn.intrinsic.ConvBnReLU1d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/ao/nn/intrinsic/modules/fused.py#L144)

This is a sequential container which calls the Conv 1d, Batch Norm 1d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.