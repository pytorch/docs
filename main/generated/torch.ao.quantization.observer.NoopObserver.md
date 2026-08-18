# NoopObserver

*class*torch.ao.quantization.observer.NoopObserver(*dtype=torch.float16*, *custom_op_name=''*)[[source]](https://github.com/pytorch/pytorch/blob/723eb3fb6c3ae1126d6b4104bb6a9c32b42e5f2e/torch/ao/quantization/observer.py#L1571)

Observer that doesn't do anything and just passes its configuration to the
quantized module's `.from_float()`.

Primarily used for quantization to float16 which doesn't require determining
ranges.

Parameters:

- **dtype** - Quantized data type
- **custom_op_name** - (temporary) specify this observer for an operator that doesn't require any observation
(Can be used in Graph Mode Passes for special case ops).