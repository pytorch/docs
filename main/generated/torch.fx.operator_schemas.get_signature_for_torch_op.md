# torch.fx.operator_schemas.get_signature_for_torch_op

torch.fx.operator_schemas.get_signature_for_torch_op(*op: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*, *return_schemas: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[Signature](https://docs.python.org/3/library/inspect.html#inspect.Signature)] | [None](https://docs.python.org/3/library/constants.html#None), [list](https://docs.python.org/3/library/stdtypes.html#list)[FunctionSchema] | [None](https://docs.python.org/3/library/constants.html#None)][[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/fx/operator_schemas.py#L226)

torch.fx.operator_schemas.get_signature_for_torch_op(*op: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [Any](https://docs.python.org/3/library/typing.html#typing.Any)]*, *return_schemas: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[False] = False*) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[Signature](https://docs.python.org/3/library/inspect.html#inspect.Signature)] | [None](https://docs.python.org/3/library/constants.html#None)

Given an operator on the torch namespace, return a list of inspect.Signature
objects corresponding to the overloads of that op.. May return None if a signature
could not be retrieved.

Parameters:

**op** (*Callable*) - An operator on the torch namespace to look up a signature for

Returns:

A list of signatures for the overloads of this

operator, or None if the operator signatures could not be retrieved. If
return_schemas=True, returns a tuple containing the optional Python signatures
and the optional TorchScript Function signature

Return type:

Optional[List[[inspect.Signature](https://docs.python.org/3/library/inspect.html#inspect.Signature)]]

Warning

This API is experimental and is *NOT* backward-compatible.