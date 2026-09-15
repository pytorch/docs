# torch.fx.operator_schemas.create_type_hint

torch.fx.operator_schemas.create_type_hint(*x*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/operator_schemas.py#L267)

Produces a type hint for the given argument.

The `create_type_hint()` looks for a type hint compatible with the input argument x.

If x is a list or tuple, it looks for an object in the list whose type is a superclass
of the rest, and uses that as base_type for the List or Tuple to be returned.
If no such object is found, it defaults to List[Any].

If x is neither a list nor a tuple, it returns x.

Warning

This API is experimental and is *NOT* backward-compatible.

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object)