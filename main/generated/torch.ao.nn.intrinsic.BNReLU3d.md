# BNReLU3d

*class*torch.ao.nn.intrinsic.BNReLU3d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/4581144c216b65e4e1b5c6eea26d4212239a231d/torch/ao/nn/intrinsic/modules/fused.py#L235)

This is a sequential container which calls the BatchNorm 3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.