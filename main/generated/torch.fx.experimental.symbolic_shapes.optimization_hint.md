# torch.fx.experimental.symbolic_shapes.optimization_hint

torch.fx.experimental.symbolic_shapes.optimization_hint(*a*, *fallback=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/experimental/symbolic_shapes.py#L177)

Return a concrete hint for a symbolic integer, for use in optimization decisions.

Unlike guarding_hint_or_throw, this function does not add guards and is intended
for optimization purposes only (e.g., memory estimation).

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int)