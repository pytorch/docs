# ConvBn3d

*class*torch.ao.nn.intrinsic.ConvBn3d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/ao/nn/intrinsic/modules/fused.py#L182)

This is a sequential container which calls the Conv 3d and Batch Norm 3d modules.
During quantization this will be replaced with the corresponding fused module.