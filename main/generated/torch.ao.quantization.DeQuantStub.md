# DeQuantStub

*class*torch.ao.quantization.DeQuantStub(*qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/ao/quantization/stubs.py#L29)

Dequantize stub module, before calibration, this is same as identity,
this will be swapped as nnq.DeQuantize in convert.

Parameters:

**qconfig** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - quantization configuration for the tensor,
if qconfig is not provided, we will get qconfig from parent modules