# torch.fx.experimental.unification.multipledispatch.variadic.isvariadic

torch.fx.experimental.unification.multipledispatch.variadic.isvariadic(*obj*)[[source]](https://github.com/pytorch/pytorch/blob/08fea85059e6f8092daa38319f7ea5bd7603d5e9/torch/fx/experimental/unification/multipledispatch/variadic.py#L36)

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