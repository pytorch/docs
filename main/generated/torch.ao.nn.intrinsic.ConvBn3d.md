# ConvBn3d

*class*torch.ao.nn.intrinsic.ConvBn3d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/ao/nn/intrinsic/modules/fused.py#L182)

This is a sequential container which calls the Conv 3d and Batch Norm 3d modules.
During quantization this will be replaced with the corresponding fused module.