# torch.mps.set_stream

torch.mps.set_stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/mps/streams.py#L91)

Set the current stream. Usage of this function is discouraged in favor
of the [`stream()`](torch.mps.stream_function.html#torch.mps.stream) context manager.

Parameters:

**stream** ([*Stream*](torch.mps.Stream_class.html#torch.mps.Stream)) - selected stream. This function is a no-op if this
argument is `None`.