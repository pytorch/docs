# torch.fx.experimental.symbolic_shapes.statically_known_true

torch.fx.experimental.symbolic_shapes.statically_known_true(*x*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/fx/experimental/symbolic_shapes.py#L1646)

Returns True if x can be simplified to a constant and is true.

Note

This function doesn't introduce new guards, so the expression may end
up evaluating to true at runtime even if this function returns False.

Parameters:

**x** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,*[*SymBool*](../torch.html#torch.SymBool)) - The expression to try statically evaluating

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)