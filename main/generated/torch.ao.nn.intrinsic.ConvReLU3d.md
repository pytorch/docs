# ConvReLU3d

*class*torch.ao.nn.intrinsic.ConvReLU3d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/ao/nn/intrinsic/modules/fused.py#L76)

This is a sequential container which calls the Conv3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.