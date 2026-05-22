# torch.fx.experimental.graph_gradual_typechecker.broadcast_types

torch.fx.experimental.graph_gradual_typechecker.broadcast_types(*t1*, *t2*)[[source]](https://github.com/pytorch/pytorch/blob/54541f51bee1b9b66a0ecb11e69067a677a60487/torch/fx/experimental/graph_gradual_typechecker.py#L83)

Applies broadcasting to both given types such that they
become consistent with each other and returns two new
resulting types

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]