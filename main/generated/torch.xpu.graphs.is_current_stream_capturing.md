# torch.xpu.graphs.is_current_stream_capturing

torch.xpu.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/xpu/graphs.py#L40)

Return True if XPU graph capture is underway on the current XPU stream, False otherwise.

If a XPU context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)