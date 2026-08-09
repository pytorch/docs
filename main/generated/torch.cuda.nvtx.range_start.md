# torch.cuda.nvtx.range_start

torch.cuda.nvtx.range_start(*msg*)[[source]](https://github.com/pytorch/pytorch/blob/a471a58d241b08025dcb4ec69c2d30e5a49a757a/torch/cuda/nvtx.py#L42)

Mark the start of a range with string message. It returns a unique handle
for this range to pass to the corresponding call to rangeEnd().

A key difference between this and range_push/range_pop is that the
range_start/range_end version supports range across threads (start on one
thread and end on another thread).

Returns: A range handle (uint64_t) that can be passed to range_end().

Parameters:

**msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - ASCII message to associate with the range.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)