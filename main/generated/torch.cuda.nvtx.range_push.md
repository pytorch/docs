# torch.cuda.nvtx.range_push

torch.cuda.nvtx.range_push(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/cuda/nvtx.py#L27)

Push a range onto a stack of nested range span. Returns zero-based depth of the range that is started.

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - ASCII message to associate with range