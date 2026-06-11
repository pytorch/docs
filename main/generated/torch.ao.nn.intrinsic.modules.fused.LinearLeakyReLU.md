# LinearLeakyReLU

*class*torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU(*linear*, *leaky_relu*)[[source]](https://github.com/pytorch/pytorch/blob/63f903c3d6b04c7cb1433d1d67e2b8e21c055bc7/torch/ao/nn/intrinsic/modules/fused.py#L269)

This is a sequential container which calls the Linear and LeakyReLU modules.
During quantization this will be replaced with the corresponding fused module.