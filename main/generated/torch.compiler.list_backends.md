# torch.compiler.list_backends

torch.compiler.list_backends(*exclude_tags=('debug', 'experimental')*)[[source]](https://github.com/pytorch/pytorch/blob/01eee25952cb32e0868ff00f26f080d46ef71e27/torch/compiler/__init__.py#L311)

Return valid strings that can be passed to torch.compile(..., backend="name").

Parameters:

**exclude_tags** (*optional*) - A tuple of strings representing tags to exclude.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]