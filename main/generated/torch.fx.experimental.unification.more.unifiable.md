# torch.fx.experimental.unification.more.unifiable

torch.fx.experimental.unification.more.unifiable(*cls*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/fx/experimental/unification/more.py#L21)

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