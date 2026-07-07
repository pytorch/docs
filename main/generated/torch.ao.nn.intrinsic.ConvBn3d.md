# ConvBn3d

*class*torch.ao.nn.intrinsic.ConvBn3d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/ao/nn/intrinsic/modules/fused.py#L182)

This is a sequential container which calls the Conv 3d and Batch Norm 3d modules.
During quantization this will be replaced with the corresponding fused module.