# torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node

torch.fx.experimental.symbolic_shapes.is_symbol_binding_fx_node(*node*)[[source]](https://github.com/pytorch/pytorch/blob/474b9649dd111ae9b0c31728da812cc3dda2c4ae/torch/fx/experimental/symbolic_shapes.py#L1108)

Check if a given FX node is a symbol binding node.

A symbol binding node is one that has a SymInt value in its meta that contains
a sympy Symbol expression, and is either a placeholder node or contains unbacked symbols.

Parameters:

**node** ([*torch.fx.Node*](../fx.html#torch.fx.Node)) - The FX node to check

Returns:

The sympy Symbol if the node is a symbol binding node, None otherwise

Return type:

Optional[sympy.Symbol]