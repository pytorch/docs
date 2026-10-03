# ConvBn1d

*class*torch.ao.nn.intrinsic.ConvBn1d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/ao/nn/intrinsic/modules/fused.py#L110)

This is a sequential container which calls the Conv 1d and Batch Norm 1d modules.
During quantization this will be replaced with the corresponding fused module.