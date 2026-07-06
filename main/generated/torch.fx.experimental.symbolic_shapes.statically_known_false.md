# torch.fx.experimental.symbolic_shapes.statically_known_false

torch.fx.experimental.symbolic_shapes.statically_known_false(*x*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/fx/experimental/symbolic_shapes.py#L1627)

Returns True if x can be simplified to a constant and is False.
If x cannot be evaluated from static, we return False

Note

This function doesn't introduce new guards, so the expression may end
up evaluating to False at runtime even if this function returns False.

Parameters:

**x** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*SymBool*](../torch.html#torch.SymBool)) - The expression to try statically evaluating

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)