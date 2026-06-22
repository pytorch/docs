# create_getattr_from_value

*class*torch.ao.quantization.fx.utils.create_getattr_from_value(*module*, *graph*, *prefix*, *value*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/2c911a1e1af237cf87c0e6e42a0fc9589043282b/torch/ao/quantization/fx/utils.py#L259)

Given a value of any type, creates a getattr node corresponding to the value and
registers the value as a buffer to the module.

Return type:

[*Node*](../fx.html#torch.fx.Node)