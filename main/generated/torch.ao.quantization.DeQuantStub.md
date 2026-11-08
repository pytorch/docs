# DeQuantStub

*class*torch.ao.quantization.DeQuantStub(*qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/ao/quantization/stubs.py#L29)

Dequantize stub module, before calibration, this is same as identity,
this will be swapped as nnq.DeQuantize in convert.

Parameters:

**qconfig** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - quantization configuration for the tensor,
if qconfig is not provided, we will get qconfig from parent modules