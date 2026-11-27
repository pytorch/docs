# torch.fx.experimental.symbolic_shapes.guard_size_oblivious

torch.fx.experimental.symbolic_shapes.guard_size_oblivious(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/5f228673c58f6d36691c0cbc5c677fdf0c349372/torch/fx/experimental/symbolic_shapes.py#L564)

Kept for existing callers; size-oblivious reasoning has been removed.

Emptiness checks on a value statically known to be >= 0 keep the old
answer ("assume non-empty"): `x == 0` uses `guard_or_false` and
`x != 0` / `x > 0` / `x >= 1` use `guard_or_true`. Every other
predicate uses `guard_bool`.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)