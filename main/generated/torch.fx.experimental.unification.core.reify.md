# torch.fx.experimental.unification.core.reify

torch.fx.experimental.unification.core.reify(*e*, *s*)[[source]](https://github.com/pytorch/pytorch/blob/80b434f9a9e9f3dd439f5883f376326e470526ff/torch/fx/experimental/unification/core.py#L53)

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

[object](https://docs.python.org/3/builtins/functions.html#object)