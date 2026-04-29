# torch.fx.experimental.unification.multipledispatch.core.dispatch

torch.fx.experimental.unification.multipledispatch.core.dispatch(**types*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/fx/experimental/unification/multipledispatch/core.py#L22)

Dispatch function on the types of the inputs
Supports dispatch on all non-keyword arguments.
Collects implementations based on the function name. Ignores namespaces.
If ambiguous type signatures occur a warning is raised when the function is
defined suggesting the additional method to break the ambiguity.

Example

```
>>> @dispatch(int)
... def f(x):
... return x + 1
>>> @dispatch(float)
... def f(x):
... return x - 1
>>> f(3)
4
>>> f(3.0)
2.0
>>> # Specify an isolated namespace with the namespace keyword argument
>>> my_namespace = {}
>>> @dispatch(int, namespace=my_namespace)
... def foo(x):
... return x + 1
>>> # Dispatch on instance methods within classes
>>> class MyClass(object):
... @dispatch(list)
... def __init__(self, data):
... self.data = data
...
... @dispatch(int)
... def __init__(self, datum):
... self.data = [datum]
>>> MyClass([1, 2, 3]).data
[1, 2, 3]
>>> MyClass(3).data
[3]
```

Return type:

Callable[[Callable[..., _T]], Callable[..., _T]]