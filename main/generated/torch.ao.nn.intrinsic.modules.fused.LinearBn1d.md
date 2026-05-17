# LinearBn1d

*class*torch.ao.nn.intrinsic.modules.fused.LinearBn1d(*linear*, *bn*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/ao/nn/intrinsic/modules/fused.py#L252)

This is a sequential container which calls the Linear and BatchNorm1d modules.
During quantization this will be replaced with the corresponding fused module.