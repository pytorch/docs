# torch.fx.experimental.symbolic_shapes.optimization_hint

torch.fx.experimental.symbolic_shapes.optimization_hint(*a*, *fallback=None*)[[source]](https://github.com/pytorch/pytorch/blob/5f228673c58f6d36691c0cbc5c677fdf0c349372/torch/fx/experimental/symbolic_shapes.py#L177)

Return a concrete hint for a symbolic integer, for use in optimization decisions.

Unlike guarding_hint_or_throw, this function does not add guards and is intended
for optimization purposes only (e.g., memory estimation).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)