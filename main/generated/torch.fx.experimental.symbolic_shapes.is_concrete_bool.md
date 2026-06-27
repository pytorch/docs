# torch.fx.experimental.symbolic_shapes.is_concrete_bool

torch.fx.experimental.symbolic_shapes.is_concrete_bool(*a*)[[source]](https://github.com/pytorch/pytorch/blob/0e9f4621713322cc25850b6b032d13bc31696736/torch/fx/experimental/symbolic_shapes.py#L481)

Utility to check if underlying object
in SymBool is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymBool*](../torch.html#torch.SymBool)*or*[*bool*](https://docs.python.org/3/library/functions.html#bool)) - Object to test if it bool

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)