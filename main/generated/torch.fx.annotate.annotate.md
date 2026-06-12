# torch.fx.annotate.annotate

torch.fx.annotate.annotate(*val*, *type*)[[source]](https://github.com/pytorch/pytorch/blob/5ffde693e13e101c8a4f5ea685dfbaef0c7e7466/torch/fx/annotate.py#L11)

Annotates a Proxy object with a given type.

This function annotates a val with a given type if a type of the val is a torch.fx.Proxy object
:param val: An object to be annotated if its type is torch.fx.Proxy.
:type val: object
:param type: A type to be assigned to a given proxy object as val.
:type type: object

Returns:

The given val.

Raises:

[**RuntimeError**](https://docs.python.org/3/library/exceptions.html#RuntimeError) - If a val already has a type in its node.

Return type:

[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)

Warning

This API is experimental and is *NOT* backward-compatible.