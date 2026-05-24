# NoopObserver

*class*torch.ao.quantization.observer.NoopObserver(*dtype=torch.float16*, *custom_op_name=''*)[[source]](https://github.com/pytorch/pytorch/blob/15e96b281415c58d3acf5d63d86df9d68744ee16/torch/ao/quantization/observer.py#L1571)

Observer that doesn't do anything and just passes its configuration to the
quantized module's `.from_float()`.

Primarily used for quantization to float16 which doesn't require determining
ranges.

Parameters:

- **dtype** - Quantized data type
- **custom_op_name** - (temporary) specify this observer for an operator that doesn't require any observation
(Can be used in Graph Mode Passes for special case ops).