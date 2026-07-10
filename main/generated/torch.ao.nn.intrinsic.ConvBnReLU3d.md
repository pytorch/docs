# ConvBnReLU3d

*class*torch.ao.nn.intrinsic.ConvBnReLU3d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/ao/nn/intrinsic/modules/fused.py#L199)

This is a sequential container which calls the Conv 3d, Batch Norm 3d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.