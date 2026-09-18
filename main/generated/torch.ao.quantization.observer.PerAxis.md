# PerAxis

*class*torch.ao.quantization.observer.PerAxis(*axis*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/ao/quantization/observer.py#L1724)

Represents per-axis granularity in quantization.

This granularity type calculates different quantization parameters
along a specified axis of the tensor.

For example if the input tensor is shape [8, 16] and axis=0, then
the quantization parameters are calculated for each row of the tensor.
Giving a total of 8 quantization parameters.

Variables:

**axis** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The axis along which reduction is performed.