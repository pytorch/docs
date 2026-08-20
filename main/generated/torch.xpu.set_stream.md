# torch.xpu.set_stream

torch.xpu.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/xpu/__init__.py#L631)

Set the current stream. This is a wrapper API to set the stream.

Usage of this function is discouraged in favor of the `stream`
context manager.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This function is a no-op
if this argument is `None`.