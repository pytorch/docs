# torch.fx.experimental.unification.multipledispatch.variadic.isvariadic

torch.fx.experimental.unification.multipledispatch.variadic.isvariadic(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/unification/multipledispatch/variadic.py#L36)

Check whether the type obj is variadic.
:param obj: The type to check
:type obj: type

Returns:

Whether or not obj is variadic

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)

Examples

```
>>> isvariadic(int)
False
>>> isvariadic(Variadic[int])
True
```