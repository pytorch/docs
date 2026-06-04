# torch.fx.experimental.symbolic_shapes.optimization_hint

torch.fx.experimental.symbolic_shapes.optimization_hint(*a*, *fallback=None*)[[source]](https://github.com/pytorch/pytorch/blob/40a42e9b743c053cc9e6d11c0502026a8f5d7d57/torch/fx/experimental/symbolic_shapes.py#L154)

Return a concrete hint for a symbolic integer, for use in optimization decisions.

Unlike guarding_hint_or_throw, this function does not add guards and is intended
for optimization purposes only (e.g., memory estimation).

Return type:

[int](https://docs.python.org/3/library/functions.html#int)