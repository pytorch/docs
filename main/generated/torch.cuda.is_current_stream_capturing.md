# torch.cuda.is_current_stream_capturing

torch.cuda.is_current_stream_capturing()[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/cuda/graphs.py#L57)

Return True if CUDA graph capture is underway on the current CUDA stream, False otherwise.

If a CUDA context does not exist on the current device, returns False without initializing the context.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)