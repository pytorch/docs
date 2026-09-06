# torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/fx/experimental/symbolic_shapes.py#L131)

Return a concrete hint for a symbolic value, for use in guarding decisions.

Returns Python bool (True/False) for boolean inputs (SymBool, bool),
and Python int for integer inputs (SymInt, int).

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool)