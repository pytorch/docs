# torch.mps.stream

torch.mps.stream(*stream*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/mps/streams.py#L66)

Context manager that selects a given stream.

MPS operators called within this context will be enqueued on the selected
stream.

Parameters:

**stream** ([*Stream*](torch.mps.Stream_class.html#torch.mps.Stream)) - selected stream. This manager is a no-op if it's `None`.