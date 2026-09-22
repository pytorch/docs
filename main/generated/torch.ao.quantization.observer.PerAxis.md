# PerAxis

*class*torch.ao.quantization.observer.PerAxis(*axis*)[[source]](https://github.com/pytorch/pytorch/blob/9d784735eb70fb8b0335b0ad7cad9db3ea4babbd/torch/ao/quantization/observer.py#L1724)

Represents per-axis granularity in quantization.

This granularity type calculates different quantization parameters
along a specified axis of the tensor.

For example if the input tensor is shape [8, 16] and axis=0, then
the quantization parameters are calculated for each row of the tensor.
Giving a total of 8 quantization parameters.

Variables:

**axis** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - The axis along which reduction is performed.