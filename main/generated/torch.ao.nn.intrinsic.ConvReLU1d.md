# ConvReLU1d

*class*torch.ao.nn.intrinsic.ConvReLU1d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/65e101a3cc8242711ae1cb467ed6cde097135821/torch/ao/nn/intrinsic/modules/fused.py#L42)

This is a sequential container which calls the Conv1d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.