# torch.fx.experimental.merge_matmul.may_depend_on

torch.fx.experimental.merge_matmul.may_depend_on(*a*, *b*, *search_depth=6*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/experimental/merge_matmul.py#L35)

Determine if one node depends on another in a torch.fx.Graph.

Parameters:

- **a** ([*Node*](../fx.html#torch.fx.Node)) - The node that may have a dependency on b.
- **b** ([*Node*](../fx.html#torch.fx.Node)) - The node that a may have a dependency on.
- **search_depth** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) - In the case of an indirect dependency, this function
searches up to this many nodes away in search of a
data dependency. If none is found, the function
makes the conservative assumption that there is a
dependency.

Returns:

True if a may depend on b, False if it definitely does not.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)