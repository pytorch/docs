# torch.mtia.set_stream

torch.mtia.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/mtia/__init__.py#L258)

Set the current stream. This is a wrapper API to set the stream.

Usage of this function is discouraged in favor of the `stream`
context manager.

Parameters:

**stream** ([*Stream*](torch.mtia.Stream_class.html#torch.mtia.Stream)) - selected stream. This function is a no-op
if this argument is `None`.