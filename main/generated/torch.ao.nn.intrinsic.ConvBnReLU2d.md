# ConvBnReLU2d

*class*torch.ao.nn.intrinsic.ConvBnReLU2d(*conv*, *bn*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/34424f27313fbcddaafe4a1a855000f17e05a260/torch/ao/nn/intrinsic/modules/fused.py#L163)

This is a sequential container which calls the Conv 2d, Batch Norm 2d, and ReLU modules.
During quantization this will be replaced with the corresponding fused module.