# torch.cuda.set_stream

torch.cuda.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/474a11a166e1313c37a9ad6f5ed0c887409d2cfc/torch/cuda/__init__.py#L838)

Set the current stream. This is a wrapper API to set the stream.

Usage of this function is discouraged in favor of the `stream`
context manager.

Parameters:

**stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This function is a no-op
if this argument is `None`.