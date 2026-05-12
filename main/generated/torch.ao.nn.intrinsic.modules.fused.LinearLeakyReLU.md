# LinearLeakyReLU

*class*torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU(*linear*, *leaky_relu*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/ao/nn/intrinsic/modules/fused.py#L269)

This is a sequential container which calls the Linear and LeakyReLU modules.
During quantization this will be replaced with the corresponding fused module.