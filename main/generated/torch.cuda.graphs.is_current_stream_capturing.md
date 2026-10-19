# torch.cuda.graphs.is_current_stream_capturing

torch.cuda.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/9d18b95219c1c16b653b5e43e8201c0d80e98b8f/torch/cuda/graphs.py#L87)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)