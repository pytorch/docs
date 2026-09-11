# torch.fx.experimental.unification.multipledispatch.variadic.isvariadic

torch.fx.experimental.unification.multipledispatch.variadic.isvariadic(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/11cc3f2c2feafe59bf1d7f19c46edaa02b3eac25/torch/fx/experimental/unification/multipledispatch/variadic.py#L36)

Check whether the type obj is variadic.
:param obj: The type to check
:type obj: type

Returns:

Whether or not obj is variadic

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

Examples

```
>>> isvariadic(int)
False
>>> isvariadic(Variadic[int])
True
```