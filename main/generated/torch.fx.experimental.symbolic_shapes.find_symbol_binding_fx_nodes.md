# torch.fx.experimental.symbolic_shapes.find_symbol_binding_fx_nodes

torch.fx.experimental.symbolic_shapes.find_symbol_binding_fx_nodes(*graph*)[[source]](https://github.com/pytorch/pytorch/blob/22790c5da3d534b53281c0866537154a47b6a1cf/torch/fx/experimental/symbolic_shapes.py#L1134)

Find all nodes in an FX graph that bind sympy Symbols.

This function scans through all nodes in the given FX graph and identifies
nodes that bind sympy Symbols (typically placeholder nodes with SymInt values).
When multiple nodes bind the same symbol, only the first occurrence is kept.

Parameters:

**graph** ([*Graph*](../fx.html#torch.fx.Graph)) - The FX graph to search for symbol binding nodes

Returns:

A dictionary mapping from sympy Symbols to their binding FX nodes

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[*Symbol*, [*Node*](../fx.html#torch.fx.Node)]