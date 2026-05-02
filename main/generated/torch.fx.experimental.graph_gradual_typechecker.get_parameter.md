# torch.fx.experimental.graph_gradual_typechecker.get_parameter

torch.fx.experimental.graph_gradual_typechecker.get_parameter(*traced*, *target*)[[source]](https://github.com/pytorch/pytorch/blob/7b5f32b1c4911f959ed9f61cd0aefb7ed57e0317/torch/fx/experimental/graph_gradual_typechecker.py#L1009)

Returns the parameter given by `target` if it exists,
otherwise throws an error.

See the docstring for `get_submodule` for a more detailed
explanation of this method's functionality as well as how to
correctly specify `target`.

Parameters:

**target** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The fully-qualified string name of the Parameter
to look for. (See `get_submodule` for how to specify a
fully-qualified string.)

Returns:

The Parameter referenced by `target`

Return type:

torch.nn.Parameter

Raises:

[**AttributeError**](https://docs.python.org/3/library/exceptions.html#AttributeError) - If the target string references an invalid
 path or resolves to something that is not an
 `nn.Parameter`