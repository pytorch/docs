# torch.fx.experimental.unification.core.reify

torch.fx.experimental.unification.core.reify(*e*, *s*)[[source]](https://github.com/pytorch/pytorch/blob/071dd4d98ee0ca692fbe0cb3e9f3b95955d73329/torch/fx/experimental/unification/core.py#L53)

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