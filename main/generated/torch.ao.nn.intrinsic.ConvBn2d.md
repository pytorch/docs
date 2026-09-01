# ConvBn2d

*class*torch.ao.nn.intrinsic.ConvBn2d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/e0942cc74d3258d28e88ec21b1e6fbaa3538e2b6/torch/ao/nn/intrinsic/modules/fused.py#L127)

This is a sequential container which calls the Conv 2d and Batch Norm 2d modules.
During quantization this will be replaced with the corresponding fused module.