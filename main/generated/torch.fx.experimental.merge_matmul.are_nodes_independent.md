# torch.fx.experimental.merge_matmul.are_nodes_independent

torch.fx.experimental.merge_matmul.are_nodes_independent(*nodes*)[[source]](https://github.com/pytorch/pytorch/blob/bb84990ad380b2b3991c759fcefffdbd0400ad85/torch/fx/experimental/merge_matmul.py#L72)

Check if all of the given nodes are pairwise-data independent.

Parameters:

**nodes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Node*](../fx.html#torch.fx.Node)*]*) - The nodes to check for data dependencies.

Returns:

True if any pair in nodes has a data dependency.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)