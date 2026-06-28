# torch.fx.experimental.unification.utils.transitive_get

torch.fx.experimental.unification.utils.transitive_get(*key*, *d*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/experimental/unification/utils.py#L25)

Transitive dict.get
>>> d = {1: 2, 2: 3, 3: 4}
>>> d.get(1)
2
>>> transitive_get(1, d)
4

Return type:

[object](https://docs.python.org/3/library/functions.html#object)