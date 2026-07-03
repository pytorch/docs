# torch.fx.experimental.unification.utils.freeze

torch.fx.experimental.unification.utils.freeze(*d*)[[source]](https://github.com/pytorch/pytorch/blob/3d5b7664e539957501eac5dad7ecab7d12aa2088/torch/fx/experimental/unification/utils.py#L113)

Freeze container to hashable form
>>> freeze(1)
1
>>> freeze([1, 2])
(1, 2)
>>> freeze({1: 2}) # doctest: +SKIP
frozenset([(1, 2)])

Return type:

[object](https://docs.python.org/3/library/functions.html#object)