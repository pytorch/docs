# torch.fx.experimental.unification.multipledispatch.utils.typename

torch.fx.experimental.unification.multipledispatch.utils.typename(*type*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/fx/experimental/unification/multipledispatch/utils.py#L126)

Get the name of type.
:param type:
:type type: Union[Type, Tuple[Type]]

Returns:

The name of type or a tuple of the names of the types in type.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

Examples

```
>>> typename(int)
'int'
>>> typename((int, float))
'(int, float)'
```