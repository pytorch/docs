# ConvBn2d

*class*torch.ao.nn.intrinsic.ConvBn2d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/ao/nn/intrinsic/modules/fused.py#L127)

This is a sequential container which calls the Conv 2d and Batch Norm 2d modules.
During quantization this will be replaced with the corresponding fused module.