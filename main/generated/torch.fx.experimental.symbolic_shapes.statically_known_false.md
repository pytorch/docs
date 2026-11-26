# torch.fx.experimental.symbolic_shapes.statically_known_false

torch.fx.experimental.symbolic_shapes.statically_known_false(*x*)[[source]](https://github.com/pytorch/pytorch/blob/f8a8dd25ad84298ffbd713e8dbdb5bba38ef907d/torch/fx/experimental/symbolic_shapes.py#L1680)

Returns True if x can be simplified to a constant and is False.
If x cannot be evaluated from static, we return False

Note

This function doesn't introduce new guards, so the expression may end
up evaluating to False at runtime even if this function returns False.

Parameters:

**x** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)*,*[*SymBool*](../torch.html#torch.SymBool)) - The expression to try statically evaluating

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)