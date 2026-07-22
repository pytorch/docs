# PerAxis

*class*torch.ao.quantization.observer.PerAxis(*axis*)[[source]](https://github.com/pytorch/pytorch/blob/964b36dfdeb2262f10adc277503b2c3dda372818/torch/ao/quantization/observer.py#L1724)

Represents per-axis granularity in quantization.

This granularity type calculates different quantization parameters
along a specified axis of the tensor.

For example if the input tensor is shape [8, 16] and axis=0, then
the quantization parameters are calculated for each row of the tensor.
Giving a total of 8 quantization parameters.

Variables:

**axis** ([*int*](https://docs.python.org/3/library/functions.html#int)) - The axis along which reduction is performed.