# torch.fx.experimental.symbolic_shapes.is_concrete_float

torch.fx.experimental.symbolic_shapes.is_concrete_float(*a*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/fx/experimental/symbolic_shapes.py#L463)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*float*](https://docs.python.org/3/builtins/functions.html#float)) - Object to test if it float

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)