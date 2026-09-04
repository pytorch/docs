# ConvReLU1d

*class*torch.ao.nn.intrinsic.ConvReLU1d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/nn/intrinsic/modules/fused.py#L42)

This is a sequential container which calls the Conv1d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.