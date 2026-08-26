# torch.fx.experimental.symbolic_shapes.statically_known_true

torch.fx.experimental.symbolic_shapes.statically_known_true(*x*)[[source]](https://github.com/pytorch/pytorch/blob/60598ed3c8773875c0923101d54f206303b2f59f/torch/fx/experimental/symbolic_shapes.py#L1660)

Returns True if x can be simplified to a constant and is true.

Note

This function doesn't introduce new guards, so the expression may end
up evaluating to true at runtime even if this function returns False.

Parameters:

**x** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*SymBool*](../torch.html#torch.SymBool)) - The expression to try statically evaluating

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)