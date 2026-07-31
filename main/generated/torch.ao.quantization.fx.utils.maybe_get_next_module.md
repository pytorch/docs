# maybe_get_next_module

*class*torch.ao.quantization.fx.utils.maybe_get_next_module(*node*, *modules*, *target_module_type=None*, *target_functional_type=None*)[[source]](https://github.com/pytorch/pytorch/blob/f613b2a0a05cebc8f0b0095458f6f2219008b0dd/torch/ao/quantization/fx/utils.py#L428)

Gets the next module that matches what is needed in
is_target_module_type if it exists

Parameters:

- **node** ([*Node*](../fx.html#torch.fx.Node)) - The node whose users we want to look at
- **target_module_type** ([*type*](https://docs.python.org/3/library/functions.html#type)*[*[*Module*](torch.nn.Module.html#torch.nn.Module)*]**|**None*) - Module type that we want to check
- **target_functional_type** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*|**None*) - Functional type that we want to check

Return type:

[*Node*](../fx.html#torch.fx.Node) | None