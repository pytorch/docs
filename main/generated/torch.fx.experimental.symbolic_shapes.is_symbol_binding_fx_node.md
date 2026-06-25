# torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node

torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/847b7df02b84551445eda7d44d08f15bda4c6159/torch/fx/experimental/symbolic_shapes.py#L1112)

Check if a given FX node is a symbol binding node.

A symbol binding node is one that has a SymInt value in its meta that contains
a sympy Symbol expression, and is either a placeholder node or contains unbacked symbols.

Parameters:

**node** ([*torch.fx.Node*](../fx.html#torch.fx.Node)) - The FX node to check

Returns:

The sympy Symbol if the node is a symbol binding node, None otherwise

Return type:

Optional[sympy.Symbol]