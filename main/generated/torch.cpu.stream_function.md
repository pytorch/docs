# torch.cpu.stream

torch.cpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/cpu/__init__.py#L215)

Wrapper around the Context-manager StreamContext that
selects a given stream.

N.B. This function only exists to facilitate device-agnostic code

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)