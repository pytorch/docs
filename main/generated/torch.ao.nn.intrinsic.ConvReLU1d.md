# ConvReLU1d

*class*torch.ao.nn.intrinsic.ConvReLU1d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/613fb8c0f7fc1641d104e1ba45491d522964094c/torch/ao/nn/intrinsic/modules/fused.py#L42)

This is a sequential container which calls the Conv1d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.