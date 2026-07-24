# torch.cpu.stream

torch.cpu.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cpu/__init__.py#L215)

Wrapper around the Context-manager StreamContext that
selects a given stream.

N.B. This function only exists to facilitate device-agnostic code

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)