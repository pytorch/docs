# torch.fx.experimental.unification.more.unify_object

torch.fx.experimental.unification.more.unify_object(*u*, *v*, *s*)[[source]](https://github.com/pytorch/pytorch/blob/7ffd47d270087d6dbafb876c0549d949aabf0a5a/torch/fx/experimental/unification/more.py#L112)

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

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[Var, [object](https://docs.python.org/3/builtins/functions.html#object)] | [bool](https://docs.python.org/3/builtins/functions.html#bool)