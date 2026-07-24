# DeQuantStub

*class*torch.ao.quantization.DeQuantStub(*qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/ao/quantization/stubs.py#L29)

Dequantize stub module, before calibration, this is same as identity,
this will be swapped as nnq.DeQuantize in convert.

Parameters:

**qconfig** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - quantization configuration for the tensor,
if qconfig is not provided, we will get qconfig from parent modules