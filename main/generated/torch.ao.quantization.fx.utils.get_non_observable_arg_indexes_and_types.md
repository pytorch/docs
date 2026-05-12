# get_non_observable_arg_indexes_and_types

*class*torch.ao.quantization.fx.utils.get_non_observable_arg_indexes_and_types(*node*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/ao/quantization/fx/utils.py#L416)

Returns a dict with of non float tensor types as keys and values which correspond to a
function to retrieve the list (which takes the node as an argument)

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[type](https://docs.python.org/3/library/functions.html#type) | [*dtype*](../tensor_attributes.html#torch.dtype), [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Node*](../fx.html#torch.fx.Node)], [list](https://docs.python.org/3/library/stdtypes.html#list)[[int](https://docs.python.org/3/library/functions.html#int)]]]