# torch.cuda.graphs.is_current_stream_capturing

torch.cuda.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/6c5b0fcd877d7b7a4a969138e85428dd95fa7636/torch/cuda/graphs.py#L87)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)