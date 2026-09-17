# get_non_observable_arg_indexes_and_types

*class*torch.ao.quantization.fx.utils.get_non_observable_arg_indexes_and_types(*node*)[[source]](https://github.com/pytorch/pytorch/blob/65c295bfa29161891e39b83fac63c4f5417ffdc2/torch/ao/quantization/fx/utils.py#L416)

Returns a dict with of non float tensor types as keys and values which correspond to a
function to retrieve the list (which takes the node as an argument)

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[type](https://docs.python.org/3/builtins/functions.html#type) | [*dtype*](../tensor_attributes.html#torch.dtype), [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Node*](../fx.html#torch.fx.Node)], [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]]