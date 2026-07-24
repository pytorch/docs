# torch.cuda.nvtx.range_push

torch.cuda.nvtx.range_push(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/cuda/nvtx.py#L27)

Push a range onto a stack of nested range span. Returns zero-based depth of the range that is started.

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - ASCII message to associate with range