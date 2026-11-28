# torch.mps.set_stream

torch.mps.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/mps/streams.py#L99)

Set the current stream. Usage of this function is discouraged in favor
of the [`stream()`](torch.mps.stream_function.html#torch.mps.stream) context manager.

Parameters:

**stream** ([*Stream*](torch.mps.Stream_class.html#torch.mps.Stream)) - selected stream. This function is a no-op if this
argument is `None`.