# PerGroup

*class*torch.ao.quantization.observer.PerGroup(*group_size*)[[source]](https://github.com/pytorch/pytorch/blob/95bac518a2d5467f21c9fc6906d33d1766a40e33/torch/ao/quantization/observer.py#L1743)

Represents per-channel group granularity in quantization.

This granularity type calculates different quantization parameters
for each group of <group_size> elements.

For example if the input tensor is shape [8, 16], and the group size is 4, then
the input tensor is reshaped to [64, 4]
quantization parameters are calculated for each group of 4 elements,
giving a total of 64 quantization parameters.

Variables:

**group_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The size of each quantization group