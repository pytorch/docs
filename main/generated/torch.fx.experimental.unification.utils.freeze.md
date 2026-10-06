# torch.fx.experimental.unification.utils.freeze

torch.fx.experimental.unification.utils.freeze(*d*)[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/fx/experimental/unification/utils.py#L113)

Freeze container to hashable form
>>> freeze(1)
1
>>> freeze([1, 2])
(1, 2)
>>> freeze({1: 2}) # doctest: +SKIP
frozenset([(1, 2)])

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object)