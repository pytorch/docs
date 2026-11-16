# torch.compiler.list_backends

torch.compiler.list_backends(*exclude_tags=('debug', 'experimental')*)[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/compiler/__init__.py#L312)

Return valid strings that can be passed to torch.compile(..., backend="name").

Parameters:

**exclude_tags** (*optional*) - A tuple of strings representing tags to exclude.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]