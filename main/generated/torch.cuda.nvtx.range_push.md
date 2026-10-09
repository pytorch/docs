# torch.cuda.nvtx.range_push

torch.cuda.nvtx.range_push(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/cuda/nvtx.py#L27)

Push a range onto a stack of nested range span. Returns zero-based depth of the range that is started.

Parameters:

**msg** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) - ASCII message to associate with range