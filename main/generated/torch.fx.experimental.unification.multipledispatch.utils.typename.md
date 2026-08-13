# torch.fx.experimental.unification.multipledispatch.utils.typename

torch.fx.experimental.unification.multipledispatch.utils.typename(*type*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/experimental/unification/multipledispatch/utils.py#L126)

Get the name of type.
:param type:
:type type: Union[Type, Tuple[Type]]

Returns:

The name of type or a tuple of the names of the types in type.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

Examples

```
>>> typename(int)
'int'
>>> typename((int, float))
'(int, float)'
```