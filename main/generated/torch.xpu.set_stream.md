# torch.xpu.set_stream

torch.xpu.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/xpu/__init__.py#L657)

Set the current stream. This is a wrapper API to set the stream.

Usage of this function is discouraged in favor of the `stream`
context manager.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This function is a no-op
if this argument is `None`.