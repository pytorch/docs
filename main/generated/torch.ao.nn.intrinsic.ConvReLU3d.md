# ConvReLU3d

*class*torch.ao.nn.intrinsic.ConvReLU3d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/ab645165510131aa973a5b8880aa56f565e59c7b/torch/ao/nn/intrinsic/modules/fused.py#L76)

This is a sequential container which calls the Conv3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.