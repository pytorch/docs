# PerAxis

*class*torch.ao.quantization.observer.PerAxis(*axis*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/quantization/observer.py#L1724)

Represents per-axis granularity in quantization.

This granularity type calculates different quantization parameters
along a specified axis of the tensor.

For example if the input tensor is shape [8, 16] and axis=0, then
the quantization parameters are calculated for each row of the tensor.
Giving a total of 8 quantization parameters.

Variables:

**axis** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The axis along which reduction is performed.