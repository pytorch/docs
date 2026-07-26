# torch.cpu.stream

torch.cpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/cpu/__init__.py#L215)

Wrapper around the Context-manager StreamContext that
selects a given stream.

N.B. This function only exists to facilitate device-agnostic code

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)