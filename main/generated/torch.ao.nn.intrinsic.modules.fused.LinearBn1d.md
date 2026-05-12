# LinearBn1d

*class*torch.ao.nn.intrinsic.modules.fused.LinearBn1d(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/ao/nn/intrinsic/modules/fused.py#L252)

This is a sequential container which calls the Linear and BatchNorm1d modules.
During quantization this will be replaced with the corresponding fused module.