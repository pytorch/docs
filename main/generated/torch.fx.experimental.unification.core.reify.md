# torch.fx.experimental.unification.core.reify

torch.fx.experimental.unification.core.reify(*e*, *s*)[[source]](https://github.com/pytorch/pytorch/blob/24e9a3928e16bb875a0a4ae3d26677dd7ddc8e02/torch/fx/experimental/unification/core.py#L65)

Replace variables of expression with substitution
>>> x, y = var(), var()
>>> e = (1, x, (3, y))
>>> s = {x: 2, y: 4}
>>> reify(e, s)
(1, 2, (3, 4))
>>> e = {1: x, 3: (y, 5)}
>>> reify(e, s)
{1: 2, 3: (4, 5)}

Return type:

[object](https://docs.python.org/3/library/functions.html#object)