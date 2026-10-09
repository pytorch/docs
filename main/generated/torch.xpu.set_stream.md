# torch.xpu.set_stream

torch.xpu.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/263689def4523511f77298ad022a780a83a5b69b/torch/xpu/__init__.py#L628)

Set the current stream. This is a wrapper API to set the stream.

Usage of this function is discouraged in favor of the `stream`
context manager.

Parameters:

**stream** ([*Stream*](torch.xpu.Stream_class.html#torch.xpu.Stream)) - selected stream. This function is a no-op
if this argument is `None`.