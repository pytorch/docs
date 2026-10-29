# torch.fx.experimental.symbolic_shapes.is_concrete_float

torch.fx.experimental.symbolic_shapes.is_concrete_float(*a*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/symbolic_shapes.py#L463)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*float*](https://docs.python.org/3/builtins/functions.html#float)) - Object to test if it float

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)