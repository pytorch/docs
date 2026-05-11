# torch.cuda.set_stream

torch.cuda.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/cuda/__init__.py#L838)

Set the current stream. This is a wrapper API to set the stream.

Usage of this function is discouraged in favor of the `stream`
context manager.

Parameters:

**stream** ([*Stream*](torch.cuda.Stream_class.html#torch.cuda.Stream)) - selected stream. This function is a no-op
if this argument is `None`.