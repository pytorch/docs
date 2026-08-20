# torch.cuda.nvtx.range

torch.cuda.nvtx.range(*msg*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/nvtx.py#L115)

Context manager / decorator that pushes an NVTX range at the beginning
of its scope, and pops it at the end. If extra arguments are given,
they are passed as arguments to msg.format().

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - message to associate with the range