# torch.fx.node.has_side_effect

torch.fx.node.has_side_effect(*fn*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/node.py#L142)

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