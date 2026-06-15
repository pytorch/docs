# maybe_get_next_module

*class*torch.ao.quantization.fx.utils.maybe_get_next_module(*node*, *modules*, *target_module_type=None*, *target_functional_type=None*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/quantization/fx/utils.py#L428)

Gets the next module that matches what is needed in
is_target_module_type if it exists

Parameters:

- **node** ([*Node*](../fx.html#torch.fx.Node)) - The node whose users we want to look at
- **target_module_type** ([*type*](https://docs.python.org/3/library/functions.html#type)*[*[*Module*](torch.nn.Module.html#torch.nn.Module)*]**|**None*) - Module type that we want to check
- **target_functional_type** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - Functional type that we want to check

Return type:

[*Node*](../fx.html#torch.fx.Node) | None