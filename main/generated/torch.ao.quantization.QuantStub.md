# QuantStub

*class*torch.ao.quantization.QuantStub(*qconfig=None*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/ao/quantization/stubs.py#L11)

Quantize stub module, before calibration, this is same as an observer,
it will be swapped as nnq.Quantize in convert.

Parameters:

**qconfig** ([*QConfig*](torch.ao.quantization.qconfig.QConfig.html#torch.ao.quantization.qconfig.QConfig)*|**None*) - quantization configuration for the tensor,
if qconfig is not provided, we will get qconfig from parent modules