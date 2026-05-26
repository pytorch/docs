# torch.fx.experimental.unification.more.unify_object

torch.fx.experimental.unification.more.unify_object(*u*, *v*, *s*)[[source]](https://github.com/pytorch/pytorch/blob/09c9b1ec9c2e88520d11a9c64b206359e8ca912b/torch/fx/experimental/unification/more.py#L112)

Unify two Python objects
Unifies their type and `__dict__` attributes
>>> class Foo(object):
... def __init__(self, a, b):
... self.a = a
... self.b = b
...
... def __str__(self):
... return "Foo(%s, %s)" % (str(self.a), str(self.b))
>>> x = var("x")
>>> f = Foo(1, x)
>>> g = Foo(1, 2)
>>> unify_object(f, g, {})
{~x: 2}

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[Var, [object](https://docs.python.org/3/library/functions.html#object)] | [bool](https://docs.python.org/3/library/functions.html#bool)