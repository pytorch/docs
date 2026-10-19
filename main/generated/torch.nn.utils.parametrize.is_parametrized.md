# torch.nn.utils.parametrize.is_parametrized

torch.nn.utils.parametrize.is_parametrized(*module*, *tensor_name=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/nn/utils/parametrize.py#L674)

Determine if a module has a parametrization.

Parameters:

- **module** ([*nn.Module*](torch.nn.Module.html#torch.nn.Module)) - module to query
- **tensor_name** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)*,**optional*) - name of the parameter in the module
Default: `None`

Returns:

`True` if `module` has a parametrization for the parameter named `tensor_name`,
or if it has any parametrization when `tensor_name` is `None`;
otherwise `False`

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)