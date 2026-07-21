# create_getattr_from_value

*class*torch.ao.quantization.fx.utils.create_getattr_from_value(*module*, *graph*, *prefix*, *value*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/ao/quantization/fx/utils.py#L259)

Given a value of any type, creates a getattr node corresponding to the value and
registers the value as a buffer to the module.

Return type:

[*Node*](../fx.html#torch.fx.Node)