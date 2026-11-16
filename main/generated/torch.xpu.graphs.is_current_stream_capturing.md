# torch.xpu.graphs.is_current_stream_capturing

torch.xpu.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/11b971398ac96eefe8b5d8296dabcc43092d8b6e/torch/xpu/graphs.py#L40)

Return True if XPU graph capture is underway on the current XPU stream, False otherwise.

If a XPU context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)