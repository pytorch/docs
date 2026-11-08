# torch.cuda.is_current_stream_capturing

torch.cuda.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/cuda/graphs.py#L87)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)