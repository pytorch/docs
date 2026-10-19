# torch.compiler.list_backends

torch.compiler.list_backends(*exclude_tags=('debug', 'experimental')*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/compiler/__init__.py#L311)

Return valid strings that can be passed to torch.compile(..., backend="name").

Parameters:

**exclude_tags** (*optional*) - A tuple of strings representing tags to exclude.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]