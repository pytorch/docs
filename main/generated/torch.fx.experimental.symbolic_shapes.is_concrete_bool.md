# torch.fx.experimental.symbolic_shapes.is_concrete_bool

torch.fx.experimental.symbolic_shapes.is_concrete_bool(*a*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fx/experimental/symbolic_shapes.py#L483)

Utility to check if underlying object
in SymBool is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymBool*](../torch.html#torch.SymBool)*or*[*bool*](https://docs.python.org/3/library/functions.html#bool)) - Object to test if it bool

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)