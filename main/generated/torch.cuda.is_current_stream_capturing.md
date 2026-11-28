# torch.cuda.is_current_stream_capturing

torch.cuda.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/cuda/graphs.py#L89)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)