# torch.fx.experimental.symbolic_shapes.is_concrete_int

torch.fx.experimental.symbolic_shapes.is_concrete_int(*a*)[[source]](https://github.com/pytorch/pytorch/blob/e1994aea9ce307fb82feeb7524ab2c5d36771e4f/torch/fx/experimental/symbolic_shapes.py#L442)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - Object to test if it int

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)