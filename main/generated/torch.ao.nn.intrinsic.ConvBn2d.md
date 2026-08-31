# ConvBn2d

*class*torch.ao.nn.intrinsic.ConvBn2d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/c9fded8194d3b089ed610b586eb746a6e74c6616/torch/ao/nn/intrinsic/modules/fused.py#L127)

This is a sequential container which calls the Conv 2d and Batch Norm 2d modules.
During quantization this will be replaced with the corresponding fused module.