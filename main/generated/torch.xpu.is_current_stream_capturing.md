# torch.xpu.is_current_stream_capturing

torch.xpu.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/2b0c4f59ccd6d695a849965e24aaadab868e2c3e/torch/xpu/graphs.py#L40)

Return True if XPU graph capture is underway on the current XPU stream, False otherwise.

If a XPU context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)