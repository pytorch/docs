# ConvBn1d

*class*torch.ao.nn.intrinsic.ConvBn1d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/ao/nn/intrinsic/modules/fused.py#L110)

This is a sequential container which calls the Conv 1d and Batch Norm 1d modules.
During quantization this will be replaced with the corresponding fused module.