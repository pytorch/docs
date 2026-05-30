# ConvBn3d

*class*torch.ao.nn.intrinsic.ConvBn3d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/ao/nn/intrinsic/modules/fused.py#L182)

This is a sequential container which calls the Conv 3d and Batch Norm 3d modules.
During quantization this will be replaced with the corresponding fused module.