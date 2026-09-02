# torch.cuda.nvtx.range

torch.cuda.nvtx.range(*msg*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/cuda/nvtx.py#L115)

Context manager / decorator that pushes an NVTX range at the beginning
of its scope, and pops it at the end. If extra arguments are given,
they are passed as arguments to msg.format().

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - message to associate with the range