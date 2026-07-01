# LinearBn1d

*class*torch.ao.nn.intrinsic.modules.fused.LinearBn1d(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/df6ed392bccc6625dbf4f6a82bcecee03433aa18/torch/ao/nn/intrinsic/modules/fused.py#L252)

This is a sequential container which calls the Linear and BatchNorm1d modules.
During quantization this will be replaced with the corresponding fused module.