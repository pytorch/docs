# torch.compiler.get_default_backend

torch.compiler.get_default_backend()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/compiler/__init__.py#L287)

Return the current default backend for `torch.compile`.

Returns:

The current default backend (string or callable). Initially `"inductor"`.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[...], [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]