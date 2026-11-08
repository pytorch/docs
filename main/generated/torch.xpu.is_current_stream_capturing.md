# torch.xpu.is_current_stream_capturing

torch.xpu.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/graphs.py#L40)

Return True if XPU graph capture is underway on the current XPU stream, False otherwise.

If a XPU context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)