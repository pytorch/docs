# ConvBnReLU1d

*class*torch.ao.nn.intrinsic.ConvBnReLU1d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/ao/nn/intrinsic/modules/fused.py#L144)

This is a sequential container which calls the Conv 1d, Batch Norm 1d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.