# ConvReLU1d

*class*torch.ao.nn.intrinsic.ConvReLU1d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/ao/nn/intrinsic/modules/fused.py#L42)

This is a sequential container which calls the Conv1d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.