# create_getattr_from_value

*class*torch.ao.quantization.fx.utils.create_getattr_from_value(*module*, *graph*, *prefix*, *value*, *device=None*)[[source]](https://github.com/pytorch/pytorch/blob/55d182046edce7face6d9eb894f23b3a2588d876/torch/ao/quantization/fx/utils.py#L259)

Given a value of any type, creates a getattr node corresponding to the value and
registers the value as a buffer to the module.

Return type:

[*Node*](../fx.html#torch.fx.Node)