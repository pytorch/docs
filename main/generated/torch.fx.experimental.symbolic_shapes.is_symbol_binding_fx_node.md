# torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node

torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/e9565720ab4f59a0ed491b3f8440ae38c2455bab/torch/fx/experimental/symbolic_shapes.py#L1151)

Check if a given FX node is a symbol binding node.

A symbol binding node is one that has a SymInt value in its meta whose
placeholder expression is a sympy Symbol, and is either a placeholder node or
records that it binds the unbacked symbol in node.meta["unbacked_bindings"].

Parameters:

**node** ([*torch.fx.Node*](../fx.html#torch.fx.Node)) - The FX node to check

Returns:

The sympy Symbol if the node is a symbol binding node, None otherwise

Return type:

Optional[sympy.Symbol]