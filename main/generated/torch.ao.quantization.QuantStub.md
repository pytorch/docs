# QuantStub

*class*torch.ao.quantization.QuantStub(*qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/ao/quantization/stubs.py#L11)

Quantize stub module, before calibration, this is same as an observer,
it will be swapped as nnq.Quantize in convert.

Parameters:

**qconfig** ([*QConfig*](torch.ao.quantization.qconfig.QConfig.html#torch.ao.quantization.qconfig.QConfig)*|**None*) - quantization configuration for the tensor,
if qconfig is not provided, we will get qconfig from parent modules