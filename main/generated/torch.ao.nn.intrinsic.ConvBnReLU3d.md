# ConvBnReLU3d

*class*torch.ao.nn.intrinsic.ConvBnReLU3d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/4581144c216b65e4e1b5c6eea26d4212239a231d/torch/ao/nn/intrinsic/modules/fused.py#L199)

This is a sequential container which calls the Conv 3d, Batch Norm 3d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.