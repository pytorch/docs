# torch.fx.experimental.unification.utils.transitive_get

torch.fx.experimental.unification.utils.transitive_get(*key*, *d*)[[source]](https://github.com/pytorch/pytorch/blob/a80ae34b7e3aa7b408f0e56e089ae40dad2c1a9a/torch/fx/experimental/unification/utils.py#L25)

Transitive dict.get
>>> d = {1: 2, 2: 3, 3: 4}
>>> d.get(1)
2
>>> transitive_get(1, d)
4

Return type:

[object](https://docs.python.org/3/library/functions.html#object)