# torch.cuda.nvtx.range

torch.cuda.nvtx.range(*msg*, **args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/nvtx.py#L115)

Context manager / decorator that pushes an NVTX range at the beginning
of its scope, and pops it at the end. If extra arguments are given,
they are passed as arguments to msg.format().

Parameters:

**msg** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - message to associate with the range