# ConvBnReLU1d

*class*torch.ao.nn.intrinsic.ConvBnReLU1d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/44a629b353df33cd84f67a031bba5b6313160a1c/torch/ao/nn/intrinsic/modules/fused.py#L144)

This is a sequential container which calls the Conv 1d, Batch Norm 1d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.