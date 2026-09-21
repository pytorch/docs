# return_arg_list

*class*torch.ao.quantization.fx.utils.return_arg_list(*arg_indices*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/ao/quantization/fx/utils.py#L376)

Constructs a function that takes a node as arg and returns the arg_indices
that are valid for node.args

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Node*](../fx.html#torch.fx.Node)], [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]