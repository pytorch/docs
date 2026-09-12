# LinearLeakyReLU

*class*torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU(*linear*, *leaky_relu*)[[source]](https://github.com/pytorch/pytorch/blob/84e524623ea4754a748936bf1ba6ecaaa92c3ae6/torch/ao/nn/intrinsic/modules/fused.py#L269)

This is a sequential container which calls the Linear and LeakyReLU modules.
During quantization this will be replaced with the corresponding fused module.