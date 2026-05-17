# torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/fx/experimental/symbolic_shapes.py#L128)

Return a concrete hint for a symbolic value, for use in guarding decisions.

Returns Python bool (True/False) for boolean inputs (SymBool, bool),
and Python int for integer inputs (SymInt, int).

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool)