# torch.compiler.get_default_backend

torch.compiler.get_default_backend()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/compiler/__init__.py#L378)

Return the current default backend for `torch.compile`.

Returns:

The current default backend (string or callable). Initially `"inductor"`.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]