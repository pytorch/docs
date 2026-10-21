# torch.fx.experimental.graph_gradual_typechecker.broadcast_types

torch.fx.experimental.graph_gradual_typechecker.broadcast_types(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/fx/experimental/graph_gradual_typechecker.py#L83)

Applies broadcasting to both given types such that they
become consistent with each other and returns two new
resulting types

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]