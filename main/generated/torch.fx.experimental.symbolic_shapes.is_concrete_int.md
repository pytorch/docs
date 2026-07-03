# torch.fx.experimental.symbolic_shapes.is_concrete_int

torch.fx.experimental.symbolic_shapes.is_concrete_int(*a*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/symbolic_shapes.py#L440)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - Object to test if it int

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)