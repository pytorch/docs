# torch.typename

torch.typename(*obj*, */*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/__init__.py#L1126)

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