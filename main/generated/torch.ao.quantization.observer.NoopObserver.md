# NoopObserver

*class*torch.ao.quantization.observer.NoopObserver(*dtype=torch.float16*, *custom_op_name=''*)[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/ao/quantization/observer.py#L1571)

Observer that doesn't do anything and just passes its configuration to the
quantized module's `.from_float()`.

Primarily used for quantization to float16 which doesn't require determining
ranges.

Parameters:

- **dtype** - Quantized data type
- **custom_op_name** - (temporary) specify this observer for an operator that doesn't require any observation
(Can be used in Graph Mode Passes for special case ops).