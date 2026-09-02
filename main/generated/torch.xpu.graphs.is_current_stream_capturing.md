# torch.xpu.graphs.is_current_stream_capturing

torch.xpu.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/4111fcac199ec5a63d637dcb967d171aa099c9d1/torch/xpu/graphs.py#L40)

Return True if XPU graph capture is underway on the current XPU stream, False otherwise.

If a XPU context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)