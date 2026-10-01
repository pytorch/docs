# torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a*)[[source]](https://github.com/pytorch/pytorch/blob/38cca96300da024842405ecefa081e4761254922/torch/fx/experimental/symbolic_shapes.py#L131)

Return a concrete hint for a symbolic value, for use in guarding decisions.

Returns Python bool (True/False) for boolean inputs (SymBool, bool),
and Python int for integer inputs (SymInt, int).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int) | [bool](https://docs.python.org/3/builtins/functions.html#bool)