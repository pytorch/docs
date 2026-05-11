# torch.cuda.graphs.is_current_stream_capturing

torch.cuda.graphs.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/cuda/graphs.py#L45)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)