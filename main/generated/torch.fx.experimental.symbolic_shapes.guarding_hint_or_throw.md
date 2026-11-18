# torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a: [SymBool](../torch.html#torch.SymBool) | [bool](https://docs.python.org/3/builtins/functions.html#bool)*) → [bool](https://docs.python.org/3/builtins/functions.html#bool)[[source]](https://github.com/pytorch/pytorch/blob/5b1433112eb30368cb8f63b3bf0145b391ec72a5/torch/fx/experimental/symbolic_shapes.py#L148)

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a: [SymInt](../torch.html#torch.SymInt) | [int](https://docs.python.org/3/builtins/functions.html#int)*) → [int](https://docs.python.org/3/builtins/functions.html#int)

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a: [SymFloat](../torch.html#torch.SymFloat) | [float](https://docs.python.org/3/builtins/functions.html#float)*) → [float](https://docs.python.org/3/builtins/functions.html#float)

torch.fx.experimental.symbolic_shapes.guarding_hint_or_throw(*a: SymNode*) → [int](https://docs.python.org/3/builtins/functions.html#int) | [bool](https://docs.python.org/3/builtins/functions.html#bool) | [float](https://docs.python.org/3/builtins/functions.html#float)

Return a concrete hint for a symbolic value, for use in guarding decisions.

Returns Python bool (True/False) for boolean inputs (SymBool, bool),
Python int for integer inputs (SymInt, int), Python float for floating-point
inputs (SymFloat, float), and for a SymNode a value matching its pytype.