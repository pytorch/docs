# ConvBn3d

*class*torch.ao.nn.intrinsic.ConvBn3d(*conv*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/a4a15a72064ca010a723eae7c73835fe206f8de6/torch/ao/nn/intrinsic/modules/fused.py#L182)

This is a sequential container which calls the Conv 3d and Batch Norm 3d modules.
During quantization this will be replaced with the corresponding fused module.