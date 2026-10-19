# torch.fx.experimental.symbolic_shapes.optimization_hint

torch.fx.experimental.symbolic_shapes.optimization_hint(*a*, *fallback=None*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/fx/experimental/symbolic_shapes.py#L157)

Return a concrete hint for a symbolic integer, for use in optimization decisions.

Unlike guarding_hint_or_throw, this function does not add guards and is intended
for optimization purposes only (e.g., memory estimation).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)