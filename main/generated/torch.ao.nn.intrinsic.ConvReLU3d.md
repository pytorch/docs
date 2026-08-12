# ConvReLU3d

*class*torch.ao.nn.intrinsic.ConvReLU3d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/ao/nn/intrinsic/modules/fused.py#L76)

This is a sequential container which calls the Conv3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.