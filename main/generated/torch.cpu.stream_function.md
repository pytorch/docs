# torch.cpu.stream

torch.cpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cpu/__init__.py#L215)

Wrapper around the Context-manager StreamContext that
selects a given stream.

N.B. This function only exists to facilitate device-agnostic code

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)