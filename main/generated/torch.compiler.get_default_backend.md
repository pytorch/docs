# torch.compiler.get_default_backend

torch.compiler.get_default_backend()[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/compiler/__init__.py#L378)

Return the current default backend for `torch.compile`.

Returns:

The current default backend (string or callable). Initially `"inductor"`.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]