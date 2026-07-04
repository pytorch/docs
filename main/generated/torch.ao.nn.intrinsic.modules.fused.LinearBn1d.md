# LinearBn1d

*class*torch.ao.nn.intrinsic.modules.fused.LinearBn1d(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/9a3243ec510ddea6c63c86d01aef273f400f375f/torch/ao/nn/intrinsic/modules/fused.py#L252)

This is a sequential container which calls the Linear and BatchNorm1d modules.
During quantization this will be replaced with the corresponding fused module.