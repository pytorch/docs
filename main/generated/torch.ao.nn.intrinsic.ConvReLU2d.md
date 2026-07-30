# ConvReLU2d

*class*torch.ao.nn.intrinsic.ConvReLU2d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/ao/nn/intrinsic/modules/fused.py#L59)

This is a sequential container which calls the Conv2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.