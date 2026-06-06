# torch.fx.experimental.unification.more.unifiable

torch.fx.experimental.unification.more.unifiable(*cls*)[[source]](https://github.com/pytorch/pytorch/blob/52b7da3f54bb5af4e72fc6040fc43f091267ad09/torch/fx/experimental/unification/more.py#L21)

Register standard unify and reify operations on class
This uses the type and __dict__ or __slots__ attributes to define the
nature of the term
See Also:
>>> class A(object):
... def __init__(self, a, b):
... self.a = a
... self.b = b
>>> unifiable(A)
<class 'unification.more.A'>
>>> x = var("x")
>>> a = A(1, 2)
>>> b = A(1, x)
>>> unify(a, b, {})
{~x: 2}

Return type:

[type](https://docs.python.org/3/library/functions.html#type)