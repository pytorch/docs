# torch.fx.experimental.symbolic_shapes.is_concrete_float

torch.fx.experimental.symbolic_shapes.is_concrete_float(*a*)[[source]](https://github.com/pytorch/pytorch/blob/a62499b17156f49891b06593215215c6df2f94b4/torch/fx/experimental/symbolic_shapes.py#L463)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - Object to test if it float

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)