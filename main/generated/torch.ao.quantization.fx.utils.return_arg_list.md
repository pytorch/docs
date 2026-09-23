# return_arg_list

*class*torch.ao.quantization.fx.utils.return_arg_list(*arg_indices*)[[source]](https://github.com/pytorch/pytorch/blob/8d6343a7cd80821d54ba546bc6f799aad9ccb79c/torch/ao/quantization/fx/utils.py#L376)

Constructs a function that takes a node as arg and returns the arg_indices
that are valid for node.args

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Node*](../fx.html#torch.fx.Node)], [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]