# torch.cpu.stream

torch.cpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cpu/__init__.py#L215)

Wrapper around the Context-manager StreamContext that
selects a given stream.

N.B. This function only exists to facilitate device-agnostic code

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)