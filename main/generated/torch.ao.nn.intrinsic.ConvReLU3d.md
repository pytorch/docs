# ConvReLU3d

*class*torch.ao.nn.intrinsic.ConvReLU3d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/ao/nn/intrinsic/modules/fused.py#L76)

This is a sequential container which calls the Conv3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.