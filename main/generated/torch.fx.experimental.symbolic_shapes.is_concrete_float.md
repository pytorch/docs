# torch.fx.experimental.symbolic_shapes.is_concrete_float

torch.fx.experimental.symbolic_shapes.is_concrete_float(*a*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/experimental/symbolic_shapes.py#L462)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*float*](https://docs.python.org/3/library/functions.html#float)) - Object to test if it float

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)