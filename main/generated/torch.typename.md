# torch.typename

torch.typename(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/__init__.py#L1512)

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