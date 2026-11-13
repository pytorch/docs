# ConvReLU2d

*class*torch.ao.nn.intrinsic.ConvReLU2d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/ao/nn/intrinsic/modules/fused.py#L59)

This is a sequential container which calls the Conv2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.