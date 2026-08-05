# LinearLeakyReLU

*class*torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU(*linear*, *leaky_relu*)[[source]](https://github.com/pytorch/pytorch/blob/e3b3670d208b9e770a7ca36a3fed1ea0f052f799/torch/ao/nn/intrinsic/modules/fused.py#L269)

This is a sequential container which calls the Linear and LeakyReLU modules.
During quantization this will be replaced with the corresponding fused module.