# torch.compiler.list_backends

torch.compiler.list_backends(*exclude_tags=('debug', 'experimental')*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L310)

Return valid strings that can be passed to torch.compile(..., backend="name").

Parameters:

**exclude_tags** (*optional*) - A tuple of strings representing tags to exclude.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]