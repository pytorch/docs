# torch.fx.experimental.unification.multipledispatch.variadic.isvariadic

torch.fx.experimental.unification.multipledispatch.variadic.isvariadic(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/c712ec6ebb4ecd2838e2cafb0bbc7a3c5acfe668/torch/fx/experimental/unification/multipledispatch/variadic.py#L36)

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