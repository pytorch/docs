# torch.compiler.list_backends

torch.compiler.list_backends(*exclude_tags=('debug', 'experimental')*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/compiler/__init__.py#L312)

Return valid strings that can be passed to torch.compile(..., backend="name").

Parameters:

**exclude_tags** (*optional*) - A tuple of strings representing tags to exclude.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]