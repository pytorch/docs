# torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node

torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/fx/experimental/symbolic_shapes.py#L1113)

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