# ConvReLU1d

*class*torch.ao.nn.intrinsic.ConvReLU1d(*conv*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/ao/nn/intrinsic/modules/fused.py#L42)

This is a sequential container which calls the Conv1d and ReLU modules.
During quantization this will be replaced with the corresponding fused module.