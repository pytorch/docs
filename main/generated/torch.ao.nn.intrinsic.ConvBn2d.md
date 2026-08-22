# ConvBn2d

*class*torch.ao.nn.intrinsic.ConvBn2d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/ao/nn/intrinsic/modules/fused.py#L127)

This is a sequential container which calls the Conv 2d and Batch Norm 2d modules.
During quantization this will be replaced with the corresponding fused module.