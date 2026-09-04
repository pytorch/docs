# DeQuantStub

*class*torch.ao.quantization.DeQuantStub(*qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/ao/quantization/stubs.py#L29)

Dequantize stub module, before calibration, this is same as identity,
this will be swapped as nnq.DeQuantize in convert.

Parameters:

**qconfig** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - quantization configuration for the tensor,
if qconfig is not provided, we will get qconfig from parent modules