# ConvBn1d

*class*torch.ao.nn.intrinsic.ConvBn1d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/nn/intrinsic/modules/fused.py#L110)

This is a sequential container which calls the Conv 1d and Batch Norm 1d modules.
During quantization this will be replaced with the corresponding fused module.