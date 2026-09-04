# torch.typename

torch.typename(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/__init__.py#L1500)

String representation of the type of an object.

This function returns a fully qualified string representation of an object's type.
:param obj: The object whose type to represent
:type obj: object

Returns:

the type of the object o

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

Example

```
>>> x = torch.tensor([1, 2, 3])
>>> torch.typename(x)
'torch.LongTensor'
>>> torch.typename(torch.nn.Parameter)
'torch.nn.parameter.Parameter'
```