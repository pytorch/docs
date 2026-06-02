# torch.fx.experimental.unification.more.reify_object

torch.fx.experimental.unification.more.reify_object(*o*, *s*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/fx/experimental/unification/more.py#L50)

Reify a Python object with a substitution
>>> class Foo(object):
... def __init__(self, a, b):
... self.a = a
... self.b = b
...
... def __str__(self):
... return "Foo(%s, %s)" % (str(self.a), str(self.b))
>>> x = var("x")
>>> f = Foo(1, x)
>>> print(f)
Foo(1, ~x)
>>> print(reify_object(f, {x: 2}))
Foo(1, 2)

Return type:

[object](https://docs.python.org/3/library/functions.html#object)