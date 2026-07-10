# torch.compiler.get_default_backend

torch.compiler.get_default_backend()[[source]](https://github.com/pytorch/pytorch/blob/01d9abd0bb0eeea5416b0ceb75d243362cc90aee/torch/compiler/__init__.py#L363)

Return the current default backend for `torch.compile`.

Returns:

The current default backend (string or callable). Initially `"inductor"`.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]