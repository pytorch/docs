# torch.fx.experimental.symbolic_shapes.is_concrete_int

torch.fx.experimental.symbolic_shapes.is_concrete_int(*a*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/fx/experimental/symbolic_shapes.py#L442)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*int*](https://docs.python.org/3/builtins/functions.html#int)) - Object to test if it int

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)