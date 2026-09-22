# LinearLeakyReLU

*class*torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU(*linear*, *leaky_relu*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/ao/nn/intrinsic/modules/fused.py#L269)

This is a sequential container which calls the Linear and LeakyReLU modules.
During quantization this will be replaced with the corresponding fused module.