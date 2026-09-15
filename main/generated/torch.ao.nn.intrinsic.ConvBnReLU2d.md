# ConvBnReLU2d

*class*torch.ao.nn.intrinsic.ConvBnReLU2d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/ao/nn/intrinsic/modules/fused.py#L163)

This is a sequential container which calls the Conv 2d, Batch Norm 2d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.