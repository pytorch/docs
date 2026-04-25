# ConvReLU2d

*class*torch.ao.nn.intrinsic.ConvReLU2d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/ao/nn/intrinsic/modules/fused.py#L59)

This is a sequential container which calls the Conv2d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.