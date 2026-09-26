# ConvBnReLU1d

*class*torch.ao.nn.intrinsic.ConvBnReLU1d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/ao/nn/intrinsic/modules/fused.py#L144)

This is a sequential container which calls the Conv 1d, Batch Norm 1d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.