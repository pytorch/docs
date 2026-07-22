# ConvReLU2d

*class*torch.ao.nn.intrinsic.ConvReLU2d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/2a8ba15825312e681c7dc6b12b79dec216aecd30/torch/ao/nn/intrinsic/modules/fused.py#L59)

This is a sequential container which calls the Conv2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.