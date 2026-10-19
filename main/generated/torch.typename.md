# torch.typename

torch.typename(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/__init__.py#L1512)

String representation of the type of an object.

This function returns a fully qualified string representation of an object's type.
:param obj: The object whose type to represent
:type obj: object

Returns:

the type of the object o

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str)

Example

```
>>> x = torch.tensor([1, 2, 3])
>>> torch.typename(x)
'torch.LongTensor'
>>> torch.typename(torch.nn.Parameter)
'torch.nn.parameter.Parameter'
```