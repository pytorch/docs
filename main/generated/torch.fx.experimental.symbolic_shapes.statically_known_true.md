# torch.fx.experimental.symbolic_shapes.statically_known_true

torch.fx.experimental.symbolic_shapes.statically_known_true(*x*)[[source]](https://github.com/pytorch/pytorch/blob/376d1c0177cbef050466ee028e0ef84f4e0d30e5/torch/fx/experimental/symbolic_shapes.py#L1655)

Returns True if x can be simplified to a constant and is true.

Note

This function doesn't introduce new guards, so the expression may end
up evaluating to true at runtime even if this function returns False.

Parameters:

**x** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*SymBool*](../torch.html#torch.SymBool)) - The expression to try statically evaluating

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)