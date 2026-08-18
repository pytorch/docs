# ConvBn1d

*class*torch.ao.nn.intrinsic.ConvBn1d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/ao/nn/intrinsic/modules/fused.py#L110)

This is a sequential container which calls the Conv 1d and Batch Norm 1d modules.
During quantization this will be replaced with the corresponding fused module.