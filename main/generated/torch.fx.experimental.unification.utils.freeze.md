# torch.fx.experimental.unification.utils.freeze

torch.fx.experimental.unification.utils.freeze(*d*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fx/experimental/unification/utils.py#L113)

Freeze container to hashable form
>>> freeze(1)
1
>>> freeze([1, 2])
(1, 2)
>>> freeze({1: 2}) # doctest: +SKIP
frozenset([(1, 2)])

Return type:

[object](https://docs.python.org/3/library/functions.html#object)