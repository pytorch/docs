# torch.fx.node.has_side_effect

torch.fx.node.has_side_effect(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/fx/node.py#L140)

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