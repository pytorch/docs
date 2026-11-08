# torch.fx.node.has_side_effect

torch.fx.node.has_side_effect(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/node.py#L144)

Registers a function to not be dead code eliminated by
fx.graph.eliminate_dead_code

NOTE: For new operators, please do not add to this set!
Instead, consider using the effects system via
torch.library._register_effectful_op() for operators.

This _side_effectful_functions set is only for:
- Legacy functions that aren't operators (e.g., profiler ops, asserts)
- Things that cannot be marked via the normal effects system

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_R*]