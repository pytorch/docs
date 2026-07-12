# torch.fx.experimental.symbolic_shapes.is_concrete_int

torch.fx.experimental.symbolic_shapes.is_concrete_int(*a*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/fx/experimental/symbolic_shapes.py#L440)

Utility to check if underlying object
in SymInt is concrete value. Also returns
true if integer is passed in.

Parameters:

**a** ([*SymInt*](../torch.html#torch.SymInt)*or*[*int*](https://docs.python.org/3/library/functions.html#int)) - Object to test if it int

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)