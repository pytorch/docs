# torch.fx.experimental.symbolic_shapes.is_concrete_bool

torch.fx.experimental.symbolic_shapes.is_concrete_bool(*a*)[[source]](https://github.com/pytorch/pytorch/blob/c96c0d945cc30cd4317ca02911049a75e43972b7/torch/fx/experimental/symbolic_shapes.py#L483)

Utility to check if underlying object
in SymBool is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymBool*](../torch.html#torch.SymBool)*or*[*bool*](https://docs.python.org/3/builtins/functions.html#bool)) - Object to test if it bool

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)