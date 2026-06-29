# BNReLU3d

*class*torch.ao.nn.intrinsic.BNReLU3d(*batch_norm*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/12a9ea264bf805a66cd87e19e767ab23c2f59fef/torch/ao/nn/intrinsic/modules/fused.py#L235)

This is a sequential container which calls the BatchNorm 3d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.