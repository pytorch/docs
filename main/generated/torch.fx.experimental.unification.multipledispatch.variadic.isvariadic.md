# torch.fx.experimental.unification.multipledispatch.variadic.isvariadic

torch.fx.experimental.unification.multipledispatch.variadic.isvariadic(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/fx/experimental/unification/multipledispatch/variadic.py#L36)

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