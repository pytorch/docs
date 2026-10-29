# torch.fx.experimental.unification.utils.freeze

torch.fx.experimental.unification.utils.freeze(*d*)[[source]](https://github.com/pytorch/pytorch/blob/f07af57fd559ef07889f363c74772ab28405da56/torch/fx/experimental/unification/utils.py#L113)

Freeze container to hashable form
>>> freeze(1)
1
>>> freeze([1, 2])
(1, 2)
>>> freeze({1: 2}) # doctest: +SKIP
frozenset([(1, 2)])

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object)