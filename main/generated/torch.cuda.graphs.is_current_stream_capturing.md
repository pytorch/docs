# torch.cuda.graphs.is_current_stream_capturing

torch.cuda.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/2dc676a67d91491beadb4615ae9fe15e144086ea/torch/cuda/graphs.py#L87)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool)