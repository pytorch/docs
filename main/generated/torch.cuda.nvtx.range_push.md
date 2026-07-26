# torch.cuda.nvtx.range_push

torch.cuda.nvtx.range_push(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/cuda/nvtx.py#L27)

Push a range onto a stack of nested range span. Returns zero-based depth of the range that is started.

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - ASCII message to associate with range