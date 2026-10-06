# LinearBn1d

*class*torch.ao.nn.intrinsic.modules.fused.LinearBn1d(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/ao/nn/intrinsic/modules/fused.py#L252)

This is a sequential container which calls the Linear and BatchNorm1d modules.
During quantization this will be replaced with the corresponding fused module.